import time

from src.extensions import celery
from celery.exceptions import Ignore
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@celery.task(bind=True)
def long_running_task(self):
    try:
        logger.info("File is being processed")
        
        progress = 0    
        while progress < 100:
            progress += 1

            task = celery.AsyncResult(self.request.id)

            while task.state == 'PAUSING' or task.state == 'PAUSED':
                self.update_state(state='PAUSED',
                                meta={'progresStatus': progress})
                # Could be done better using threading....
                time.sleep(0.1)
                
            # if self.is_aborted():
            #     # respect aborted state, and terminate gracefully.
            #     self.update_state(state='ABORTED', meta={'progresStatus': progress})
            #     print("ABORTING TASK")
            #     logger.warning('Task aborted')
            #     return
                
            if task.state == 'RESUME':
                self.update_state(state='PROCESSING')
            
            self.update_state(state='PROCESSING',
                            meta={'progresStatus': progress})
            time.sleep(0.5)
            
        logger.info('Task complete')
        return {'status': 'Task completed!', 'progresStatus': progress}
    except Exception as ex:
        self.update_state(state='FAILURE')
        raise Ignore()

@celery.task
def log(message):
    logger.debug(message)
    logger.info(message)
    logger.warning(message)
    logger.error(message)
    logger.critical(message)