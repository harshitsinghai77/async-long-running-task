package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"sync"
	"time"
)

type jobMap struct {
	sync.Mutex
	job map[string]context.CancelFunc // A CancelFunc tells an operation to abandon its work. https://golang.org/pkg/context/#CancelFunc
}

func newJobMap() *jobMap {
	return &jobMap{
		job: make(map[string]context.CancelFunc),
	}
}

func (j *jobMap) Get(key string) (value context.CancelFunc, ok bool) {
	j.Lock()
	result, ok := j.job[key]
	j.Unlock()
	return result, ok
}

func (j *jobMap) Set(key string, value context.CancelFunc) {
	j.Lock()
	j.job[key] = value
	j.Unlock()
}

func (j *jobMap) Delete(key string) {
	j.Lock()
	delete(j.job, key)
	j.Unlock()
}

// create global jobs map with cancel function
var jobs = newJobMap()

// the pretend worker will be wrapped here
func work(ctx context.Context, id string) {

	progress := 0

	for progress < 100 {
		select {
		case <-ctx.Done():
			fmt.Printf("Cancelling job id %s\n", id)
			return
		case <-time.After(time.Second):
			fmt.Printf("Job ID %s {progrss: %d} \n", id, progress)
			progress++
			time.Sleep(5 * time.Millisecond)
		}
	}
	fmt.Printf("Job ID %s {progrss: %d} \n", id, progress)
}

func helloWorldHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello World!")
}

func scheduleJobHandler(w http.ResponseWriter, r *http.Request) {

	id := fmt.Sprintf("%d", len(jobs.job)+1)
	_, ok := jobs.Get(id)
	if ok {
		fmt.Fprintf(w, "Already started job id: %s\n", id)
		return
	}

	ctx, cancel := context.WithCancel(context.Background())
	jobs.Set(id, cancel)

	go work(ctx, id)

	fmt.Fprintf(w, "Job id: %s has been started\n", id)
}

func terminateJobHandler(w http.ResponseWriter, r *http.Request) {

	id := r.URL.Query().Get("id")
	cancel, ok := jobs.Get(id)
	if !ok {
		fmt.Fprintf(w, "Job id: %s is not running\n", id)
		return
	}

	cancel()
	jobs.Delete(id)

	fmt.Fprintf(w, "Job id: %s has been canceled\n", id)
}

func main() {
	fmt.Printf("Starting server at port 8080\n")
	http.HandleFunc("/schedule", scheduleJobHandler)
	http.HandleFunc("/terminate", terminateJobHandler)
	http.HandleFunc("/", helloWorldHandler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
