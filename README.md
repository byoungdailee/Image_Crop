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

디렉토리 구조에서 실행 시 Parameter.txt 파일의 입력된 

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
원하는 Patch size와 stride, 대상이 되는 데이터셋이 있는 디렉토리 경로에 있는 이미지를 대상으로 Crop된 이미지를 사용자가 작성한 output_directory에 해당하는 디렉토리를  생성 후 저장한다.

위의 Parameter.txt 파일을 수정 시 작성한 값에 맞게 Crop된 이미지를 생성한다.

작동 예시 : Output Floder.

사용된 데이터셋 : [ISTD_Dataset](https://drive.google.com/file/d/1I0qw-65KBA6np8vIZzO6oeiOvcDBttAY/view)
