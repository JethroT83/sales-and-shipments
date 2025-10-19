from inertia import share
import settings


def inertia_share(get_response):
  def middleware(request):
    share(request,
      app_name=settings.APP_NAME,
      user=lambda: request.user,
    )

    return get_response(request)
  return middleware




# from inertia import share
# from settings import APP_NAME

# def inertia_shared_props(get_response):
#     def middleware(request):
#
#
#
#         # props = {
#         #     "auth": lambda: {
#         #         "user": (
#         #             {
#         #                 "id": request.user.id,
#         #                 "name": request.user.get_full_name() or request.user.get_username(),
#         #                 "email": request.user.email,
#         #             }
#         #             if request.user.is_authenticated
#         #             else None
#         #         )
#         #     }
#         # }
#         #
#         # share(props)
#         return get_response(request)
#     return middleware


# def inertia_shared_props(get_response):
    # def share(request):
    #     return {
    #         'appName': APP_NAME,
    #         'auth': {
    #             "user": lambda : {
    #                 "id": request.user.id,
    #                 "name": request.user.get_full_name() or request.user.get_username(),
    #                 "email": request.user.email,
    #             }
    #         }
    #     }
    #

