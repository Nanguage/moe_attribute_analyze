import os

class HtmlOutputer(object):

    def output_data(self, data):
        if not os.path.exists("../datas"):
            os.mkdir("../datas")
        file = open("../datas/"+data["title"],"w")
        # print("[INFO][outputer]file opened!")
        file.write("url:\n"+data["url"]+"\n")
        # print("url outputed!")
        file.write("data:\n"+data["content"])
        # print("content outputed!")
        file.close()

    def output_metadata(self, count_all, count_downloaded):
        file = open("../datas/meta-data", "w")
        file.write("page_num:\n%s\n"%(count_all))
        file.write("downloaded_num:\n%s\n" % (count_downloaded))
        file.close()
