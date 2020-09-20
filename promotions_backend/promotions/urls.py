from promotions.viewsets import PromotionLogViewSet

def register_routes(router):
    router.register(
        r'promotion',
        PromotionLogViewSet,
        basename='promotion'
    )
