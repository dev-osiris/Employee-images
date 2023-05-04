from flask import Flask,request, render_template
from flask_cors import CORS
import employee_pred

app = Flask(__name__)
CORS(app)

@app.route("/")
def default():
  return render_template('index.html')


# features of the model
features = ['dept code', 'gender', 'trainings', 'age', 'ratings', 'service_len', 'kpi', 'awards', 'avg train scr']


@app.route("/",methods=['POST'])
def return_prediction():
  degree = request.form.get("feature2", type=int)
  gender = request.form.get("feature3", type=int)
  trainings = request.form.get("feature4", type=int)
  age = request.form.get("feature5", type=int)
  ratings = request.form.get("feature6", type=int)
  service_len = request.form.get("feature7", type=int)
  kpi = request.form.get("feature8", type=int)
  awards = request.form.get("feature9", type=int)
  avg_train_scr = request.form.get("feature10", type=int)

  # since dept code feature doesn't matter much, we can hardcode it any value from 1 - 3  
  sample = [3, degree, gender, trainings, age, ratings, service_len, kpi,
            awards, avg_train_scr]

  try:
    # creating a total score column
    sample.append(ratings + kpi + awards)

    # creating a Metric of Sum
    sample.append(avg_train_scr * ratings)

    # make prediction using predict() method of employee_pred.py
    ans = int(employee_pred.predict([sample]))

    if ans == 1:
      ans_str = "EMPLOYEE_PROMOTED"
    else:
      ans_str = "EMPLOYEE_NOT_PROMOTED"

    return render_template('index.html', entry=ans_str)

  except TypeError:
    return render_template('index.html', entry="BAD_INPUT")


if __name__ == "__main__":
    app.run()
