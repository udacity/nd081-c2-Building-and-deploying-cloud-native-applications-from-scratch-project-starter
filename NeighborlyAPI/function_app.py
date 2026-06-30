import azure.functions as func

app = func.FunctionApp()

# Import function modules so the v2 host discovers them.
import createAdvertisement
import deleteAdvertisement
import getAdvertisement
import getAdvertisements
import getPost
import getPosts
import updateAdvertisement
import eventHubTrigger
