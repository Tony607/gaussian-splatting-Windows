@echo off
pip install torch==2.0.1+cu118 -f https://download.pytorch.org/whl/torch_stable.html
pip install plyfile tqdm
pip install submodules/diff-gaussian-rasterization
pip install submodules/simple-knn