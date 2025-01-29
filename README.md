<html lang="ja">
    <head>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1><center>重回帰</center></h1>
        <h2>なにものか？</h2>
        <p>
            CatBoostRegressor, ExtraTreesRegressor, NGBoostRegressor を使って重回帰を試すプログラムです。<br>
            <br>
            サンプルデータ：『イノベーションとAI』という本に載っていたサンプル<br>
            <a href="http://web.sfc.keio.ac.jp/~takefuji/ice.csv">http://web.sfc.keio.ac.jp/~takefuji/ice.csv</a><br>
            ・説明変数：最高気温、通行人数<br>
            ・目的変数：アイスクリームの売上<br>
            ・お題：アイスクリーム売上＝f(最高気温, 通行人数)となる関数 f を求めよ。<br>
            説明変数×2種類＋目的変数×1種類なので、まずは 3次元グラフでデータを眺めてみる。<br>
            <br>
            <img src="images/input_data.gif"><br>
            ・通行人数が 9,000 付近だと最高温度と売上は負の相関がありそう。<br>
            ・通行人数と売上は、正の相関がありそう。<br>
            <img src="images/CarBoostRegressor.gif"><br>
            ・通行人数が7,000以下では、最高温度と売上は正の相関がありそう。<br>
        </p>
        <h2>環境構築方法</h2>
        <p>
            pip install -r src\requirements.txt<br>
            <br>
        </p>
        <h2>使い方</h2>
        <h3>CatBoost Regressor</h3>
        <p>
            ・学習～モデルのセーブ～プロット<br>
            　python src\train_CatBoostRegressor.py<br>
            <br>
            ・モデルのロード～売上予測<br>
            　python src\predict_CatBoostRegressor.py (最高気温) (通行人数) [(モデルファイル名)]<br>
        </p>
        <h3>ExtraTrees Regressor</h3>
        <p>
            ・学習～モデルのセーブ～プロット<br>
            　python src\train_ExtraTreesRegressor.py<br>
            <br>
            ・モデルのロード～売上予測<br>
            　python src\predict_ExtraTreesRegressor.py (最高気温) (通行人数) [(モデルファイル名)]<br>
        </p>
        <h3>NGBoost Regressor</h3>
        <p>
            ・学習～モデルのセーブ～プロット<br>
            　python src\train_NGBoostRegressor.py<br>
            <br>
            ・モデルのロード～売上予測<br>
            　python src\predict_NGBoostRegressor.py (最高気温) (通行人数) [(モデルファイル名)]<br>
        </p>
    </body>
</html>
