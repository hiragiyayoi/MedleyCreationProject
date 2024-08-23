import librosa
import soundfile as sf
import numpy as np
import os

def create_medley_from_folder(folder_path, output_dir, output_file, extensions=(".wav", ".mp3", ".ogg")):
    """
    指定したフォルダ内の楽曲を順番につなげてメドレーを作成する

    Args:
        folder_path (str): 楽曲が入ったフォルダのパス
        output_file (str): 出力ファイルパス
        extensions (tuple): 処理対象とするファイルの拡張子 (タプルで指定)
    """
    
    # 出力先のディレクトリを作成 (存在しない場合)
    output_path = os.path.join(output_dir, output_file)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 指定したフォルダ内のファイルを拡張子でフィルタリングして取得
    files = [f for f in os.listdir(folder_path) if f.endswith(tuple(extensions))]

    
    # 出力ファイルのフルパス
    output_path = os.path.join(output_dir, output_file)

    # ファイルパスを生成
    file_paths = [os.path.join(folder_path, f) for f in files]


    # 各楽曲を読み込む
    audio_data = []
    for file_path in file_paths:
        try:
            y, sr = librosa.load(file_path)
            audio_data.append(y)
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            continue

    # 読み込んだデータを結合
    medley = np.concatenate(audio_data, axis=0)

    # メドレーを書き出す
    sf.write(output_path, medley, sr)

# 使用例
folder_path = "../music-list"
output_dir = "../output-music"  # 出力先のディレクトリ名
output_file = "medley.wav"
create_medley_from_folder(folder_path, output_dir, output_file)