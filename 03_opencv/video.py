import cv2

class Video:
    def __init__(self, src):
        self.cap = cv2.VideoCapture(src)

    # iterator 객체
    def __iter__(self):
        return self

    def __next__(self):
        ret, image = self.cap.read()
        if ret:
            return image
        else:
            raise StopIteration
    
    # context manager 객체
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, trace_back):
        if self.cap and self.cap.isOpened():
            print('video release-----')
            self.cap.release()
            cv2.destroyAllWindows()
    
    @staticmethod
    def show(image, exit_char=ord('q')):
        cv2.imshow('frame',image)
        if cv2.waitKey(1) & 0xFF == exit_char:
            return False
        return True
    
    @staticmethod
    def to_jpg(frame, quality=80):
        encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),quality]
        is_success, jpg = cv2.imencode(".jpg", frame, encode_param)
        return jpg



# from time import sleep

# v = Video(0)
# for image in v:
#     print(image.shape)
#     sleep(1)

# with Video(0) as v:
#     for ix, image in enumerate(v):
#         if ix == 5:
#             break
#         print(ix, image.shape)
#         sleep(1)

# print('종료')

# with Video(0) as v:
#     for image in v:
#         if not Video.show(image): break
#         jpg = Video.to_jpg(image)
#         print(type(jpg), jpg.shape, len(jpg))