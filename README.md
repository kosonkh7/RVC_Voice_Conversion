# RVC_Voice_Conversion

<br>

## Project Overview
VITS 기반 음성 변환 프레임워크 RVC(Retrieval-based-Voice-Conversion-WebUI)를 활용하여 듣기 좋은 AI 커버곡을 생성한다.<br>

음성 변환(Voice Conversion)이란, Source Speaker의 음성을 Target Speaker의 음성으로 변환하는 것이다.<br>

변환의 핵심은 음성의 언어적 내용(linguistic contents)은 유지한 채로, 화자의 음성 특징(리듬, 음역, 음색 등)만을 변환하는 것이다.<br>

현재 대중음악 시장에서 과거에 인기를 끌었던 곡을 요즘 트렌드에 맞춰 재해석한 리메이크 곡 시장이 활발하다.<br>

이에 따라 특정 가수가 특정 곡을 부르면 어떤 느낌으로 와닿을지 듣길 바라는 수요가 늘어나고 있다.<br>

궁금증을 간접적으로나마 해결해보기 위하여 개성있는 음색을 지닌 가수 A와 가수 B의 음성 데이터를 바탕으로<br>

음성 변환 인공지능을 활용하여 얼마나 자연스러운 품질의 커버곡을 생성하고, <br>

음악을 사랑하는 듣는이들의 수요를 만족할 수 있을지 직접 실험해보고자 한다.<br>

<br>

## Model Selection
음성합성(Text-to-Speech)분야에서 SOTA급 성능을 보이는<br>
[VITS](https://github.com/jaywalnut310/vits) (Variational Inference with adversarial learning for end-to-end Text-to-Speech) 기반 [RVC](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) 프레임워크를 사용하였다.

[![Open In Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)](https://colab.research.google.com/drive/1iWOLYE9znqT6XE5Rw2iETE19ZlqpziLx?usp=sharing)

VITS는 2023년 7월 기준으로 LJSpeech 데이터셋을 활용한 음성합성에서 Audio Quality MOS(Mean Opinion Score) 2위(4.43)을 기록하고 있는 모델이다.<br>

![image](https://github.com/kosonkh7/RVC_Voice_Conversion/assets/83086978/3fcd3c17-ed1c-4d3a-ada7-f8633fb4ae3b)

위 모델에서  posterior encoder, decoder 그리고 conditional prior로 이루어진 conditional VAE 구조를 확인할 수 있다.

<br>

## Data Collection
가수 A와 가수 B의 음성 데이터 각각 20~30분 분량으로 준비하였다.<br>

데이터의 분량이 중요한 이유는,
모델 학습 시에 가능한 많은 음운과 음역대를 입력해주어야, 음성 변환 시 자연스러운 결과물이 따라오길 기대할 수 있기 때문이다.<br>

그렇지 않으면 발음이 어색하거나, 특정 음역대는 기계음으로 대체되는 경우가 부지기수이다.

<br>

## Data Preprocessing

![image](https://github.com/kosonkh7/RVC_Voice_Conversion/assets/83086978/7a973547-6ccf-4b44-89c2-0a8012f059a2)

학습 데이터셋을 구성할 음성 데이터와, 레퍼런스가 될 음성 데이터는 모두 아래와 같은 방법으로 전처리해준다.<br>
전처리는 [Ultimate Vocal Remover](https://github.com/Anjok07/ultimatevocalremovergui) 을 활용하였고, 사용 방법은 링크 첨부한다.<br>

1. 원본 데이터(노래)에서 배경음악 분리 [(전처리1)](https://kosonkh7.tistory.com/167)<br>

2. 분리된 음성 데이터에서 코러스 추출 및 제거 [(전처리2)](https://kosonkh7.tistory.com/173)<br>

3. De-reberb 적용 (선택) [(전처리3)](https://kosonkh7.tistory.com/170)<br>

De-reberb 적용하면 데이터 품질이 떨어진다는 의견도 보았지만,<br>

경우에 따라선 De-reberb 적용해주어야 발음이 정확하게 잡히거나, 잡음이 주는 경향을 보였기에 잘 판단하면 좋을 것 같다.<br>

본인은 모델 학습 시 사용되는 데이터는 에코를 제거하지 않고, 추가적으로 학습 시간 단축을 위해 앞뒤 공백 부분을 trim하였고<br>

레퍼런스로 사용되는 데이터는 에코를 제거하는 방식으로 활용하였다.<br>

<br>

## Model Training

ㅡ과정
모델 선정 (+ 피쳐 셀렉션 알고리즘 이해)
모델 학습
학습된 모델 분석

ㅡ마무리
결과물 공유
결론 및 느낀점
