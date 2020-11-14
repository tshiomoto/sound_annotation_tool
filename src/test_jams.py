import sys
sys.path.append("../src")

import jams
import librosa


# 音声読み込み
wav_path = "sample/sample_sound.wav"
data, sr = librosa.load(wav_path, sr=None)

# Compute the track duration
track_duration = librosa.get_duration(y=data, sr=sr)

# JAMSの作成・設定
jam = jams.JAMS()
jam.file_metadata.duration = track_duration

# アノテーションラベルの作成
annotation = jams.Annotation(namespace='lyrics')
annotation.annotation_metadata = jams.AnnotationMetadata(data_source='test annotate')

# アノテーションの追加
annotation.append(time=6.32, duration=0.5, value="くしゃみ")
annotation.append(time=9.65, duration=0.21, value="くしゃみ")

# アノテーションラベルをJAMSに追加
jam.annotations.append(annotation)

# アノテーション情報を保存
jam.save("output/test.jams")