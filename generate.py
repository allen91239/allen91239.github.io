#python html generator

 #https://bit.ly/nlp-amt-data
import pandas as pd
if __name__ == "__main__":
    df = pd.read_csv("./lab4-data.csv") 
    title = df.idx.to_list()
    corpus = df.text.to_list()
    
    for i in range(len(df)):
        f = open(f'hit{i}.html','wb')
        data = corpus[i]
        wordcount = data.split(' ')
        counttime = int(len(wordcount))
        message = f"""<!doctype html>
<html lang="en"><head>
	<meta content="text/html;charset=UTF-8" http-equiv="Content-Type">
	<script src="https://s3.amazonaws.com/mturk-public/externalHIT_v1.js" type="text/javascript"></script>
    <style>p.solid {'{border-style: dotted; font-weight: bold;}'}</style>
</head>
<body>
	<form id="mturk_form" method="post" name="mturk_form" action="https://www.mturk.com/mturk/externalSubmit">
		<input type="hidden" id="assignmentId" value="" name="assignmentId">

		<h2>After reading the tweet, choose from the options below how the tweet feels.</h2>
		<br>
		<p class="solid">{data}</p>
		<br>
        <div class="solid">
		<p>Select from 1~5 for Valence</p>
		<input type="radio" id="unpleasant" name="valence" value="unpleasant" required>
		<label for="unpleasant">(1) Unpleasant</label><br>
		<input type="radio" id="unsatisfied" name="valence" value="unsatisfied">
		<label for="unsatisfied">(2) Unsatisfied</label><br>
		<input type="radio" id="neutral" name="valence" value="neutral">
		<label for="neutral">(3) Neutral</label><br>
		<input type="radio" id="pleased" name="valence" value="pleased">
		<label for="pleased">(4) Pleased</label><br>
		<input type="radio" id="pleasant" name="valence" value="pleasant">
		<label for="pleasant">(5) Pleasant</label><br>
		<p>Select from 1~5 for Arousal</p>
		<input type="radio" id="calm" name="arousal" value="calm" required>
		<label for="calm">(1) Calm</label><br>
		<input type="radio" id="dull" name="arousal" value="dull">
		<label for="dull">(2) Dull</label><br>
		<input type="radio" id="neutral" name="arousal" value="neutral">
		<label for="neutral">(3) Neutral</label><br>
		<input type="radio" id="wideawake" name="arousal" value="wideawake">
		<label for="wideawake">(4) Wide-awake</label><br>
		<input type="radio" id="excited" name="arousal" value="excited">
		<label for="excited">(5) Excited</label><br>
		<p>Select from 1~5 for Dominance</p>
		<input type="radio" id="independent" name="dominance" value="independent" required>
		<label for="independent">(1) Independent</label><br>
		<input type="radio" id="powerful" name="dominance" value="powerful">
		<label for="powerful">(2) Powerful</label><br>
		<input type="radio" id="neutral" name="dominance" value="neutral">
		<label for="neutral">(3) Neutral</label><br>
		<input type="radio" id="powerlessness" name="dominance" value="powerlessness">
		<label for="powerlessness">(4) Powerlessness</label><br>
		<input type="radio" id="dependent" name="dominance" value="dependent">
		<label for="dependent">(5) Dependent</label><br>
        </div>
		<br>
        <p id="timeLeft"></p>
		<input type="submit" id="submitButton" disabled="disabled" value="submit">
	</form>
	<script language="Javascript">turkSetAssignmentID();</script>
    </body>
<script type="text/javascript">
    var countdownNum = {counttime};
    """
        script = """

    window.onload=function() {
      incTimer();
    }

    function incTimer(){
      setTimeout (function(){
        if(countdownNum != 0){
          countdownNum--;
          document.getElementById('timeLeft').innerHTML = 'Time left: ' + countdownNum + ' seconds. Please read it through.';
          incTimer();
        } else {
          document.getElementById('submitButton').disabled = null;
          document.getElementById('timeLeft').innerHTML = 'Ready to submit!';
        }
      },1000);
    }
</script>
</html>
"""
        message = message + script
        message = message.encode()
        f.write(message)
        f.close()
