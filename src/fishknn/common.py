

def load_df():
    """
    저장된 csv파일이 있는지 확인하고 DataFrame형식으로 반환합니다.
    """
    if os.path.exists(f"{filepath}/data/fish.csv"):
        df = pd.read_csv(f"{filepath}/data/fish.csv")
        df = df[["Length","Weight","Label"]]
    else:
        df = pd.DataFrame({"Length":[],"Weight":[],"Label":[]})

    return df

def load_pkl():
    if os.path.exists(f"{filepath}/model/model.pkl"):
        with open(f"{filepath}/model/model.pkl", "rb") as f:
            knn=pickle.load(f)
    else:
        print("⛔ 훈련된 pkl파일이 없습니다.\n⛔ 모델 훈련 후 다시 확인해주세요.")
        knn=None    
    
    return knn