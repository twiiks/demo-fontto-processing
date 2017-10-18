프로세스
------------------------
process -> fontto_pix2pix -> (written2all -> one2classes -> generator), (store2S3)

함수
------------------------

1. 입력
    - prosess()
        -  서버 전체를 다루는 파이썬 파일
        -  REQUEST를 받아 핵심 함수 (fontto_pix2pix)를 실행하고 RESPONSE

2. 프로세스
    - generator()
        - pix2pix를 활용해 하나의 이미지로 하나의 결과 생성
        - 입력 : image (입력이미지 pytorch tensor float 타입), path_pth
        - 출력 : image (생성이미지 PIL 타입)
        - EXAMPlE
            - 붐 -> 폰
    - one2class()
        - 하나의 unicode, image쌍을 입력받아 해당 unicode로 만들 수 있는 모든 글자를 generator 함수를 이용해 생성
        - 입력 : unicode, image
        - 출력 : {'unicode' : image}
        - EXAMPlE
            - 붐 -> 폰, 톤, 풀, 틀 ...
    - written2all()
        - unicode, url쌍들을 입력받아 하나씩 one2classes 함수를 이용해 생성
        - 입력 : {'unicode' : image}
        - 출력 : {'unicode' : image}
        - nxEXAMPlE
            - (붐 -> 폰, 폰, 풀...), (누 -> 구, 루, 로, ...), ... ,(휅 -> 봵, 왥, ...)
    - store2S3()
        - 생성된 이미지를 S3에 저장
        - 입력 : {'unicode' : image}, count
        - 출력 : {'unicode' : url}
    - fontto_pix2pix()
        - written2all 함수를 이용해 이미지 생성 후 store2S3 함수를 이용해 S3에 저장
        - 입력 : {'urls' : {'unicode' : url}, 'count' : count}
        - 출력 : {'urls' : {'unicode' : url}, 'count' : count}

3. 유틸리티
    - urls2imgs()
        - fontto_pix2pix에서 사용할 수 있도록 url을 통해 이미지를 로드하고 PIL Image로 변환하여 반환
        - 입력 : url
        - 반환 : image

