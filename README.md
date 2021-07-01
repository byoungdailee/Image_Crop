# Image Stride and Patch Size 별로 분할.
이미지 파일을 원하는 stride와 patch size를 기준으로 자르기 위한 .py

crop.py 을 실행한 전체 디렉토리 구조는 다음과 같이 되어있다.
```bash
├── train
│   ├── train_A
│   ├── train_B
│   └── train_C
├── test
│   ├── test_A
│   ├── test_B
│   └── test_C
├── crop.py
└── Parameter.txt
``` 

디렉토리 구조에서 실행 시 아래의 정보대로 Parameter.txt 파일을 읽어들여 실행된다.

```
Parameter.txt Example.
patch_x_size = 64
patch_y_size = 48
stride = 10
input_A_directory = train/train_A
input_B_directory = train/train_B
input_C_directory = train/train_C
output_directory = Output
```
원하는 Patch size와 stride, 대상이 되는 데이터셋이 있는 디렉토리 경로에 있는 이미지를 대상으로 

Crop된 이미지를 사용자가 작성한 output_directory에 해당하는 디렉토리를  생성 후 저장한다.

구조 예시 : Output 디렉토리 구조
```bash
├── (output_directory)
│   ├── (대상이 되는 파일 명)_(stride)_(patch_x_size)_(patch_y_size)
│         ├── (대상이 되는 파일 명)_(stride)_(patch_x_size)_(patch_y_size)_(A)
│         │  ├── (대상이 되는 파일 명)_(stride)_(patch_x_size)_(patch_y_size)_(x축 반복 횟수)_(y축 반복 횟수)_(A)
│         ├── (대상이 되는 파일 명)_(stride)_(patch_x_size)_(patch_y_size)_(B)
│         │  ├── (대상이 되는 파일 명)_(stride)_(patch_x_size)_(patch_y_size)_(x축 반복 횟수)_(y축 반복 횟수)_(B)_(하얀색 화소수의 개수)
│         └── (대상이 되는 파일 명)_(stride)_(patch_x_size)_(patch_y_size)_(C)
│              └── (대상이 되는 파일 명)_(stride)_(patch_x_size)_(patch_y_size)_(x축 반복 횟수)_(y축 반복 횟수)_(C)
...
``` 

위의 Parameter.txt 파일의 대상 파일의 경로, stride, patch size를 읽어들여 Crop된 이미지를 생성한다.

해당되는 데이터셋 중 train_B는 그림자 매트에 해당하기 때문의 전체 이미지에서의 white 화소수를 파일명에 추가로 저장하였다.

작동 예시 : Output Floder.

사용된 데이터셋 : [ISTD_Dataset](https://drive.google.com/file/d/1I0qw-65KBA6np8vIZzO6oeiOvcDBttAY/view)
