import csv

from bs4 import BeautifulSoup
import requests

repo_number = 0

finalized_repos = {
    "https://github.com/pytorch/serve",
    "https://github.com/alibaba/spring-cloud-alibaba",
    "https://github.com/LMAX-Exchange/disruptor",
    "https://github.com/open-telemetry/opentelemetry-java-instrumentation",
    "https://github.com/airbytehq/airbyte",
    "https://github.com/apache/incubator-doris",
    "https://github.com/TeamNewPipe/NewPipe",
    "https://github.com/testcontainers/testcontainers-java",
    "https://github.com/redis/jedis",
    "https://github.com/skylot/jadx",
    "https://github.com/Netflix/conductor",
    "https://github.com/apache/calcite",
    "https://github.com/OpenFeign/feign",
    "https://github.com/baomidou/mybatis-plus",
    "https://github.com/grpc/grpc-java",
    "https://github.com/azkaban/azkaban",
    "https://github.com/airbnb/lottie-android",
    "https://github.com/ReactiveX/RxAndroid",
    "https://github.com/crossoverJie/JCSprout",
    "https://github.com/json-path/JsonPath.git",
    "https://github.com/square/moshi",
    "https://github.com/termux/termux-app",
    "https://github.com/Netflix/zuul",
    "https://github.com/square/picasso",
    "https://github.com/pagehelper/Mybatis-PageHelper",
    "https://github.com/square/retrofit",
    "https://github.com/Tencent/tinker",
    "https://github.com/greenrobot/greenDAO",
    "https://github.com/resilience4j/resilience4j",
    "https://github.com/zhoutaoo/SpringCloud.git",
    "https://github.com/wildfirechat/server",
    "https://github.com/Netflix/eureka",
    "https://github.com/google/auto",
    "https://github.com/iBotPeaches/Apktool",
    "https://github.com/PhilJay/MPAndroidChart",
    "https://github.com/mapstruct/mapstruct",
    "https://github.com/clojure/clojure",
    "https://github.com/yidongnan/grpc-spring-boot-starter",
    "https://github.com/signalapp/Signal-Android",
    "https://github.com/JSQLParser/JSqlParser",
    "https://github.com/apache/incubator-shenyu",
    "https://github.com/spring-projects/spring-petclinic",
    "https://github.com/LuckSiege/PictureSelector",
    "https://github.com/alibaba/arthas",
    "https://github.com/apache/iceberg",
    "https://github.com/zo0r/react-native-push-notification",
    "https://github.com/linkedin/datahub",
    "https://github.com/apache/zeppelin",
    "https://github.com/Tencent/QMUI_Android",
    "https://github.com/dropwizard/metrics",
    "https://github.com/AsyncHttpClient/async-http-client",
    "https://github.com/alibaba/canal",
    "https://github.com/Qihoo360/RePlugin",
    "https://github.com/sshahine/JFoenix",
    "https://github.com/xuxueli/xxl-job",
    "https://github.com/asLody/VirtualApp",
    "https://github.com/dromara/hutool",
    "https://github.com/apache/shardingsphere-elasticjob",
    "https://github.com/apolloconfig/apollo",
    "https://github.com/real-logic/aeron",
    "https://github.com/CymChad/BaseRecyclerViewAdapterHelper",
    "https://github.com/alibaba/druid",
    "https://github.com/square/javapoet",
    "https://github.com/react-native-image-picker/react-native-image-picker",
    "https://github.com/koral--/android-gif-drawable",
    "https://github.com/pxb1988/dex2jar",
    "https://github.com/cryptomator/cryptomator",
    "https://github.com/Tencent/APIJSON",
    "https://github.com/PaperMC/Paper",
    "https://github.com/LawnchairLauncher/lawnchair",
    "https://github.com/PojavLauncherTeam/PojavLauncher",
    "https://github.com/exadel-inc/CompreFace",
    "https://github.com/freyacodes/Lavalink",
    "https://github.com/android-hacker/VirtualXposed",
    "https://github.com/bumptech/glide",
    "https://github.com/linlinjava/litemall",
    "https://github.com/huanghongxun/HMCL",
    "https://github.com/alibaba/easyexcel",
    "https://github.com/gedoor/MyBookshelf",
    "https://github.com/halo-dev/halo",
    "https://github.com/jeecgboot/jeecg-boot",
    "https://github.com/macrozheng/mall",
    "https://github.com/facebook/fresco",
    "https://github.com/metersphere/metersphere",
    "https://github.com/kiwibrowser/src.next",
    "https://github.com/LSPosed/LSPosed",
    "https://github.com/M66B/NetGuard",
    "https://github.com/questdb/questdb",
    "https://github.com/wiremock/wiremock",
    "https://github.com/eclipse-vertx/vert.x",
    "https://github.com/knowm/XChange",
    "https://github.com/redisson/redisson",
    "https://github.com/quarkusio/quarkus",
    "https://github.com/strimzi/strimzi-kafka-operator",
    "https://github.com/ElderDrivers/EdXposed",
    "https://github.com/rubenlagus/TelegramBots",
    "https://github.com/traccar/traccar",
    "https://github.com/andOTP/andOTP",
    "https://github.com/xuexiangjys/XUI",
    "https://github.com/tarunsinghofficial/HacktoberFest"
}

def access_finalized_repo(repo_number):
    for repo in finalized_repos:
        repo_number = repo_number + 1
        print("Accessing repo number")
        print(repo_number)
        get_repo_info(repo)

def get_repo_info(repo):
    page = requests.get(repo)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        repository_name = soup.find_all('strong', class_="mr-2 flex-self-stretch")
        name = repository_name[0].getText().split()[0]
        commit_elements = soup.find_all('span', class_="d-none d-sm-inline")
        commits = commit_elements[1].getText().split()[0].replace(',', '')
        star_elements = soup.find_all('a', class_="social-count js-social-count")
        stars = star_elements[0].getText().split()[0]
        if stars.find('k')!=-1:
            stars=float(stars[:-1])*1000
        fork_elements = soup.find_all('a', class_="social-count")
        forks = fork_elements[1].getText().split()[0]
        if forks.find('k') != -1:
            forks = float(forks[:-1]) * 1000
    except IndexError:
        commits= "0" 
        stars= "0" 
        forks= "0" 

    writer.writerow(
        [
            name,
            repo,
            commits,
            stars,
            forks
            ]
    )

if __name__ == '__main__':
    with open('final_repo_data.csv', mode='w') as result_file:
        writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Repository Name", "URL", "Commits", "Stars", "Forks"])
        access_finalized_repo(repo_number)