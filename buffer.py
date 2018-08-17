def recent():
    from tracker.models import Buffer

    buffer = Buffer.objects.order_by(created_date)

    return buffer[-1]

def all():
    from tracker.models import Buffer
                                                                                                                                            
    buffer = Buffer.objects.order_by(created_date)
                                                                                                                                            
    return buffer
