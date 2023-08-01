# RVC_Voice_Conversion

## Project Overview
VITS 기반 음성 변환 프레임워크 RVC(Retrieval-based-Voice-Conversion-WebUI)를 활용하여 듣기 좋은 AI 커버곡을 생성한다.

음성 변환(Voice Conversion)이란, Source Speaker의 음성을 Target Speaker의 음성으로 변환하는 것이다.
변환의 핵심은 음성의 언어적 내용(linguistic contents)은 유지한 채로, 화자의 음성 특징(리듬, 음역, 음색 등)만을 변환하는 것이다.
현재 대중음악 시장에서 과거에 인기를 끌었던 곡을 요즘 트렌드에 맞춰 재해석한 리메이크 곡 시장이 활발하다.
이에 따라 특정 가수가 특정 곡을 부르면 어떤 느낌으로 와닿을지 듣길 바라는 수요가 늘어나고 있다.
궁금증을 간접적으로나마 해결해보기 위하여 개성있는 음색을 지닌 가수 A와 가수 B의 음성 데이터를 바탕으로
음성 변환 인공지능을 활용하여 얼마나 자연스러운 품질의 커버곡을 생성하고, 
음악을 사랑하는 듣는이들의 수요를 만족할 수 있을지 직접 실험해보고자 한다.

## Model Selection
음성합성(Text-to-Speech)분야에서 SOTA급 성능을 보이는 [VITS](https://github.com/jaywalnut310/vits) (Variational Inference with adversarial learning for end-to-end Text-to-Speech) 기반 [RVC](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) 프레임워크를 사용하였다.

[![Open In Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)](https://colab.research.google.com/drive/1iWOLYE9znqT6XE5Rw2iETE19ZlqpziLx?usp=sharing)

VITS는 2023년 7월 기준으로 LJSpeech 데이터셋을 활용한 음성합성에서 Audio Quality MOS(Mean Opinion Score) 2위(4.43)을 기록하고 있는 모델이다.

![image](https://github.com/kosonkh7/RVC_Voice_Conversion/assets/83086978/3fcd3c17-ed1c-4d3a-ada7-f8633fb4ae3b)

위 모델에서  posterior encoder, decoder 그리고 conditional prior로 이루어진 conditional VAE 구조를 확인할 수 있다.

## Data Collection
가수 A와 가수 B의 음성 데이터 각각 20~30분 분량으로 준비하였다.
데이터의 분량이 중요한 이유는,
모델 학습 시에 가능한 많은 음운과 음역대를 입력해주어야, 음성 변환 시 자연스러운 결과물이 따라오길 기대할 수 있기 때문이다.
그렇지 않으면 발음이 어색하거나, 특정 음역대는 기계음으로 대체되는 경우가 부지기수이다.


## Data Preprocessing



ㅡ과정
데이터셋 수집
데이터셋 전처리
모델 선정 (+ 피쳐 셀렉션 알고리즘 이해)
모델 학습
학습된 모델 분석

ㅡ마무리
결과물 공유
결론 및 느낀점
