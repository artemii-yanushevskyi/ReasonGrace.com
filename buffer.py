from tracker.models import Buffer
buffers = Buffer.objects.order_by('created_date')
for buffer in buffers:
    print(buffer.text)                                                                                                           
