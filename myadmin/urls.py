#!/usr/bin/env python
# coding=utf-8

import time
import logging

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

from django.conf.urls import include, url
from django.conf import settings
from django.views.static import serve as serve_media
# Uncomment the next two lines to enable the admin:
import xadmin
xadmin.autodiscover()

# from xadmin.plugins import xversion
# xversion.register_models()

urlpatterns = [
    url(r'^comments/', include('django_comments.urls')),
    url(r'', include(xadmin.site.urls)),
]
if settings.DEBUG:
    urlpatterns += [url(r'^media/(?P<path>.*)$', serve_media, {'document_root': settings.MEDIA_ROOT})]


if True:
    logger = logging.getLogger("default")



    def job_listener(event):
        if event.exception:
            logger.info('apscheduler_job_crashed',
                        extra={"event": str(event.job_id),
                               "exception": str(event.exception),
                               "traceback": str(event.traceback)})
        else:
            logger.info('apscheduler_job_worked',
                        extra={"event": str(event.job_id)})


    import socket

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = "".join([time.strftime("%y%m"), "9"])
        sock.bind(("127.0.0.1", int(port)))
    except socket.error:
        logger.info("scheduler_already_started, DO NOTHING")  # 避免执行多次
    else:
        if True:
            logger.info("scheduler_started")

            scheduler = BackgroundScheduler(timezone='Asia/Shanghai')
            from django_apscheduler.jobstores import DjangoJobStore

            scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')

            scheduler.add_listener(job_listener,
                                   EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

            from app.cron import cronjob
            # 广告任务状态
            scheduler.add_job(cronjob, 'interval', seconds=60,
                              id="cronjob", replace_existing=True)

            # 任务分析相关
            # scheduler.add_job(timing_analyzer, 'cron', hour=4, minute=10,
            #                   id="timing_analyzer", replace_existing=True)
            # scheduler.add_job(analytics_task, 'interval', seconds=1200,
            #                   id="analytics_task", replace_existing=True)
            # scheduler.add_job(realtime_analytics_task, 'interval', seconds=300,
            #                   id="realtime_analytics_task",
            #                   replace_existing=True)
            # scheduler.add_job(analytics_previous_day, 'cron', hour="8-12",
            #                   minute=35, id="analytics_previous_day",
            #                   replace_existing=True)
            # scheduler.add_job(channel_realtime_data_task, 'cron',
            #                   minute=50, id="channel_realtime_data_task",
            #                   replace_existing=True)
            # scheduler.add_job(daily_analytics_task, 'cron', hour=2, minute=30,
            #                   id="channel_realtime_data_task",
            #                   replace_existing=True)

            # # 同步数据任务
            # scheduler.add_job(kepler_async_job_task, 'interval', hours=3,
            #                   id="kepler_async_job_task", replace_existing=True)
            # scheduler.add_job(kepler_ranking_task, 'cron', hour=3, minute=1,
            #                   id="kepler_ranking_task", replace_existing=True)

            # # 站内消息状态
            # scheduler.add_job(daily_income_port_task, 'cron', hour=3, minute=1,
            #                   id="daily_income_port_task",
            #                   replace_existing=True)
            # scheduler.add_job(message_flow_del_task, 'cron', hour=4, minute=1,
            #                   id="message_flow_del_task", replace_existing=True)
            # scheduler.add_job(create_user_ref_task, 'interval', seconds=1200,
            #                   id="create_user_ref_task", replace_existing=True)

            # # 大咖活动通知
            # scheduler.add_job(promote_new_task, 'cron', hour=2, minute=1,
            #                   id="promote_new_task", replace_existing=True)

            # # 提现备注任务
            # scheduler.add_job(present_feedback_handle, 'interval', seconds=600,
            #                   id="present_remark_handle", replace_existing=True)

            # # 大数据量导出任务
            # scheduler.add_job(big_data_export_task, 'interval', seconds=300,
            #                   id="big_data_export_task", replace_existing=True)

            # # 截图任务审核通过加钱
            # scheduler.add_job(task_picture_admin_task, 'interval', seconds=300,
            #                   id="task_picture_admin_task",
            #                   replace_existing=True)

            # # 大咖提现记录误杀恢复
            # scheduler.add_job(present_biggie_cheat_pass, 'cron',
            #                   hour=15, minute=1, id="present_biggie_cheat_pass",
            #                   replace_existing=True)

            scheduler.start()
            logger.info("apscheduler_add_job_over")
