import datetime #파일 저장시 시간정보도 함께 저장하기 위해서 사용
import openpyxl
from Modules.tools import p
max_size_of_uuids = 2  # uuids 리스트의 최대 크기(가변)
uuids = [""] * max_size_of_uuids  # 매도,매수 주문에 대한 uuid를 저장하는 list
size_of_uuids = 0 # UUID loads size
access_key = "" # ACCESS_KEY
secret_key = "" # SCERET_KEY

def get_uuid(index):
    # uuids에서 특정 index의 uuid 값을 반환하는 함수
    # > input: 가져올 인덱스 값
    # > output: uuid (type=str)
    return str(uuids[index]) #혹시라서 Wrapper로 감싸줌
def get_sizeOfUuids():
    return size_of_uuids
def get_maxSizeOfUuids():
    return max_size_of_uuids
def set_sizeOfUuids(size):
    global size_of_uuids
    size_of_uuids = size
    return size_of_uuids
def set_maxSizeOfUuids(size):
    global max_size_of_uuids
    max_size_of_uuids = size
    return max_size_of_uuids
def uuids_dataIn(input_uuid):
    # uuids에 데이터를 넣는 함수
    # > input = uuid 값
    # > output = 해당 값이 들어간 uuids
    global size_of_uuids
    global uuids
    if get_sizeOfUuids() == max_size_of_uuids:
        resize_uuids()
        #p("resize")
    uuids[size_of_uuids] = str(input_uuid)
    set_sizeOfUuids(size_of_uuids+1)
    return uuids[size_of_uuids-1]
def resize_uuids():
    # uuids 크기가 초기화 했던 사이즈를 넘어가면 resize 해주는 함수, 기존 maxsize의 두배로 늘려줌
    # > input: X , 전역변수 값 활용
    # > output: resize된 uuids
    global uuids
    global size_of_uuids
    global max_size_of_uuids
    new_maxSizeOfUuids = get_maxSizeOfUuids()*2
    res_list = [""] * new_maxSizeOfUuids
    for i in range (get_sizeOfUuids()):
        res_list[i] = get_uuid(i)
    uuids = res_list
    set_maxSizeOfUuids(new_maxSizeOfUuids)
    return uuids
def save_uuidsToTxtFile():
    # uuids를 인덱스 순서대로 file에 저장해주는 함수
    now = datetime.datetime.now()
    f = open ('uuids.txt', 'a+', encoding ='UTF8')
    for i in range (size_of_uuids):
        f.write(f"{now}>> {i}. uuids[{i}]: {uuids[i]}\n")
def save_toExcel():
    return None
