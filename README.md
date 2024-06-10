# RVC_Voice_Conversion
<font size = 10> [음성 변환 결과물 모음 링크](https://www.youtube.com/@ky-melody) </font>

<br>

## Project Overview
**VITS 기반 음성 변환 프레임워크 RVC를 활용하여 듣기 좋은 AI 커버곡을 생성한다.** <br>


음성 변환(Voice Conversion)이란, Source Speaker의 음성을 Target Speaker의 음성으로 변환하는 것이다.<br>

변환의 핵심은 **음성의 언어적 내용(linguistic contents)은 유지한 채로, 화자의 음성 특징(리듬, 음역, 음색 등)만을 변환**하는 것이다.<br>

현재 대중음악 시장에서 과거에 인기를 끌었던 곡을 요즘 트렌드에 맞춰 재해석한 리메이크 곡 시장이 활발하다.<br>

이에 따라 특정 가수가 특정 곡을 부르면 어떤 느낌으로 와닿을지 듣길 바라는 수요가 늘어나고 있다.<br>

궁금증을 간접적으로나마 해결해보기 위하여 개성있는 음색을 지닌 가수 A와 가수 B의 음성 데이터를 바탕으로<br>

음성 변환 인공지능을 활용하여 얼마나 자연스러운 품질의 커버곡을 생성하고, <br>

음악을 사랑하는 듣는이들의 수요를 만족할 수 있을지 직접 실험해보고자 한다.<br>

<br>

## Model Selection
음성합성(Text-to-Speech)분야에서 SOTA급 성능을 보이는 [VITS](https://github.com/jaywalnut310/vits) (Variational Inference with adversarial learning for end-to-end Text-to-Speech) 기반 [RVC](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) (Retrieval-based-Voice-Conversion-WebUI) 프레임워크를 사용하였다.

VITS는 2023년 7월 기준으로 [LJSpeech](https://keithito.com/LJ-Speech-Dataset/) 데이터셋을 활용한 음성합성에서 Audio Quality MOS(Mean Opinion Score) 2위(4.43)을 기록하고 있다.<br>

![image](https://github.com/kosonkh7/RVC_Voice_Conversion/assets/83086978/3fcd3c17-ed1c-4d3a-ada7-f8633fb4ae3b)

위 모델에서  posterior encoder, decoder 그리고 conditional prior로 이루어진 conditional VAE 구조를 확인할 수 있다.

<br>

## Data Collection
가수 A와 가수 B의 음성 데이터 각각 20~30분 분량으로 준비하였다.<br>

데이터의 분량이 중요한 이유는, 모델 학습 시에 가능한 많은 음운과 음역대를 입력해주어야,<br>

음성 변환 시 자연스러운 결과물이 따라오길 기대할 수 있기 때문이다.<br>

그렇지 않으면 발음이 어색하거나, 특정 음역대는 기계음으로 대체되는 경우가 부지기수이다.<br>

몇 차례 실험 결과 음성 데이터 분량은 20분이면 충분하였다.<br>

모델 학습 시간이 데이터셋 분량에 비례하므로, 비용적 측면까지 고려하여 30분 기준으로 데이터 수집하는 걸 권장한다.<br>

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

[![Open In Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)](https://colab.research.google.com/drive/1iWOLYE9znqT6XE5Rw2iETE19ZlqpziLx?usp=sharing)<br>

모델 학습 및 음성 변환 방법은 개인 블로그에 정리하여 포스팅 하였다. 아래 링크 첨부.<br>

[[RVC Web UI 설치 및 실행 방법]](https://kosonkh7.tistory.com/166) <br>

[[학습 및 음성 변환 가이드]](https://kosonkh7.tistory.com/168) <br>

피치 추출 알고리즘(pitch extraction algorithm)으로는 [CREPE](https://arxiv.org/abs/1802.06182)(Convolutional Representation for Pitch Estimation)을 사용하였고,<br>

500 에포크 학습하여 loss/d/total 이 가장 낮은 부근의 모델을 음성 변환에 활용하였다.<br>


![image](https://github.com/kosonkh7/RVC_Voice_Conversion/assets/83086978/e4ea3e27-363a-4a63-8fc5-31dd64e253f8)<br>

![image](https://github.com/kosonkh7/RVC_Voice_Conversion/assets/83086978/27ae4bfb-b812-4ce0-b40a-280e8c5ae949)<br>


## Conclusion

[가수 A모델 - 들리나요](https://youtu.be/NiTndFI5SGs)<br>

[가수 A모델 - 첫눈처럼 너에게 가겠다](https://youtu.be/Wk77DKsDB4c)<br>

[가수 B모델 - 눈의 꽃](https://youtu.be/Bn3S86hrunk)<br>

결과물은 정량적인 평가보다는 정성적인 평가가 수반된다.<br>

변환 결과로 선명한 음이 나오더라도, 원하는 음색과 창법이 반영되지는 않았을 수 있기 때문이다.<br>

모델 A와 모델 B를 바탕으로 수십 곡 정도를 생성해보면서 느낀 점은<br>

모델 학습에 사용된 데이터와 레퍼런스 데이터 사이에 음역대와 창법이 유사할수록 자연스럽게 결과가 나왔다.<br>

특히 레퍼런스가 되는 데이터의 음성 특징 (발음 등)의 개성이 독특한 경우,<br>

결과물에 강하게 반영되어 원하는 결과물을 얻기 어려운 경우가 많았기 때문에,<br>

이를 고려하여 깔끔한 발성과 창법에서 비롯된 곡을 선정해서 변환하면 좋은 결과를 얻길 기대하기 좋다.<br>

본 프로젝트에서는 AI 기반 기술을 활용하여 데이터 전처리 하였는데,<br>

미디(Musical Instrument Digital Interface)를 활용한 믹싱 기술이 병행된다면(MR 분리, 노이즈 제거, 옥타브 변환 등) 보다 듣기 좋은 결과를 기대할 수 있을 것이다.<br>

## Reference

[Mangio-RVC-Fork](https://github.com/Mangio621/Mangio-RVC-Fork)<br>

[Ultimate Vocal Remover GUI](https://github.com/Anjok07/ultimatevocalremovergui)<br>

[VITS](https://github.com/jaywalnut310/vits)<br>
