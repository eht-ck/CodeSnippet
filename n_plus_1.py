#N+1 Problem
users = User.objects.all()  # 1 Query

for user in users:
    orders = user.orders.all()  # N Queries (One per user)
# select_related()
users = User.objects.select_related('orders').all()  # 1 Query
# prefetch_related()
users = User.objects.prefetch_related('orders').all()  # 2 Queries (Optimized)
