from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing

from chat import consumers


application = ProtocolTypeRouter({

	'websocket': AuthMiddlewareStack(
		URLRouter(
			chat.routing.websocket_urlpatterns
		)
	),
})