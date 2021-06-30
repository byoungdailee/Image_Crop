# Image Stride and Patch 별로 분할.
이미지 파일을 stride와 patch size로 자르기 위한 프로그램

crop.py 을 해당 레포 디렉토리 구조에서 실행 시 Parameter.txt 파일의 입력된 

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
을 기준으로 Crop된 이미지를 생성한다.

작동 예시 : OutputImage Floder.

사용된 데이터셋 : [ISTD_Dataset](https://drive.google.com/file/d/1I0qw-65KBA6np8vIZzO6oeiOvcDBttAY/view)
