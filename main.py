import crawling
import write_data
from apscheduler.schedulers.background import BlockingScheduler

# main 실행부
def operating_main():
    print('operating main work')
    crawling.run_crawling()

    goods_total_url_list = crawling.get_goods_total_url_list()

    goods_total_detail_info_list = crawling.get_total_goods_detail_info(goods_total_url_list)

    write_data.write_goods_total_data(goods_total_detail_info_list)

    write_data.write_category()

    write_data.write_brand()

#######################################
#
# by. JaeHyeon (22/11/12)
# main = Crawling & Write Data 스케줄링 
# args ->
# scheduler.add_job(operating_main, 'cron', hour=3, id='main_work')
# operating_main 함수를 매주 금요일 오전 3시에 해당 id 값을 갖고 실행
# 
#######################################
def main():
    scheduler = BlockingScheduler(timezone='Asia/Seoul')
    scheduler.add_job(operating_main, 'cron', day_of_week=4, hour=3, id='main_work')
    scheduler.start()
    
if __name__ == '__main__':
    main()