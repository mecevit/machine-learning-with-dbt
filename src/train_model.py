from layer.decorators import model, dataset
import layer

layer.login()
layer.init("mecevit-sandbox")


df = ref(context.current_model.name)


@dataset("passengers_from_dbt")
def register_dataset():
    return df


# Register dbt model to Layer
register_dataset()


@model(name='survival_model_with_dbt')
def train():
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split

    test_size = 0.3
    random_state = 42
    n_estimators = 100

    layer.log({"test_size": test_size,
               "random_state" : random_state,
               "n_estimators": n_estimators})

    df = layer.get_dataset("passengers_from_dbt").to_pandas()
    X = df.drop(["Survived"], axis=1)
    y = df["Survived"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    random_forest = RandomForestClassifier(n_estimators=n_estimators)
    random_forest.fit(X_train, y_train)
    return random_forest


# Train model on Layer infra with the registered dbt model
layer.run([train])