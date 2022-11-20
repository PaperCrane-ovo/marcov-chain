# marcov-chain
According to a probability_matrix to create music
北京大学2022音乐与数学小组研究课题4:根据马尔科夫链生成随机音乐
## To start
use `pip install -r requirements.txt` to install dependences
```
pip install numpy

git clone https://github.com/mdoege/PySynth.git
cd PySynth
python setup.py install
```
## To use
统计出一段音乐中的音级转移概率,将音级转移概率矩阵保存在歌曲名.txt中,会自动根据转移概率矩阵生成一段音乐保存在歌曲名.wav中.


**成品可在cpp_version/wav中找到**
