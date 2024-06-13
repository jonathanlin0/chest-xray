This repository holds the important files related to our group's work for the CS156b class. We ended up getting **_3rd place_** on the evaluation leaderboard (before the final presentation was given).

The challenge of the class was to classify 9 pathologies from given chest x-rays. We initially tried a multi-class classification approach, but found that having a single model for each pathology and view (lateral vs frontal), though inefficient, performed the best.

These files are meant to serve as inspiration for students or researchers attempting to solve similar problems. They are not meant to be directly downloaded and run, since the specific directories of data, labels, etc can change from year to year. But for reference, the context of the python scripts were run from the parent of the parent of our group's folder - the CS156B folder.

There are a variety of useful figures in the `/figs` folder. `/labels` contains the outputs generated from `cnn.py`. `/visualization` contains a few scripts used to generate the figures.

We also tried using GANs to generate images of the minority classes (the dataset is heavily imbalanced) and to provide more data for vision transformers, but we couldn't get this to work.

## Spring Force

Aside from the usual CNN approach to classifying the pathologies, we found that using the labels of pathologies that are highly correlated with the target pathology to influence the label of a target pathology significantly reduced the MSE of certain pathologies that conventional ML models couldn't solve.

The file is called ``apply_spring.py`` because influencing the target pathology's label can be thought of as multiple pathologies having springs attached to the target pathology. Then based on a variety of factors, the helper pathologies apply differing amounts of force (influence) on the target pathology. Things that influenced the spring force included, but weren't limited to, the MSE of the helper category and correlation factor. And they were applied in the ways that you would expect. The lower the MSE of the helper pathology, the greater the influence because that indicated that the helper pathology label was more likely to be correct. The higher the magnitude of the correlation factor, the greater the infleunce. You can read through the file to see all of the factors that infleunce the spring force.

## Important Files

`transfer_trained_to_csv.py` transfers a model's output into the evaluation phase csv file.

`CNN.py` runs a model with a ResNet152 (pretrained on ImageNet) in the front and a linear layer afterward to predict the labels of a given pathology from an image. It has a variety of command-line arguments that you can read at the top of the file. The file contains the Dataset objects, the Dataloaders, the preprocessing, the model, and the training loop. Note: it is bad practice to put all of these items in a single file, but this class was only 10 weeks long and we weren't going to use these scripts again, so we didn't bother with best practices.

`apply_spring.py` alters a given pathology's labels for the evaluation data based on labels of pathologies that are highly correlated with the target pathology.

`/figs/corr.png` shows the correlation matrix based on the training data. Useful for `apply_spring.py`.


## Training data indices: <br>
0 no finding <br>
1 enlarged cardiomediastinum <br>
2 Cardiomegaly <br>
3 Lung opacity <br>
4 Pneumonia <br>
5 Pleural effusion <br>
6 Pleural other <br>
7 Fracture <br>
8 Support devices <br>

## Test data indices:  <br>
1 enlarged cardiomediastinum <br>
2 no finding <br>
3 cardiomegaly <br>
4 pleural effusion <br>
5 pneumonia <br>
6 lung opacity <br>
7 pleural other <br>
8 fracture <br>
9 support devices <br>