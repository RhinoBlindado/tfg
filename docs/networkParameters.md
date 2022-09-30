# MeshCNN Parameters

## General
---
#### `dataroot PATH`
Path to dataset (should have subfolders train, test). 

Required.

#### `dataset_mode classification|segmentation>`
Mode of operation. 

Default is `classification`.

#### `ninput_edges INT`
Number of input edges to the network. 

Default is `750`.

#### `max_dataset_size INT`
Maximum number of samples per epoch. 

Default is infinity.

#### `batch_size INT`
Input batch size. 

Default is `16`.

#### `arch STR`
Type of network.

Default is `mvconvnet`.

#### `resblocks INT`
Number of residual blocks in convolutional layers. 

Default is `0`.

#### `fc_n INT [INT ...]`
Number (how many numbers) and density (each number) of fully connected layers between the convolutional blocks and the SoftMax classifier. 

Default is `100`.

Number of layers has to match `dropout` number.

#### `dropout FLOAT [FLOAT ...]`
Number (how many numbers) and percentage (each number) of dropout for each fully connecte layer. 

Default is `0`.

Number of layers has to match `fc_n` number.


#### `nfc INT [INT ...]`
Number (how many numbers) and density (each number) of convolutional layers. 

Default is `16 32 32`. 

Number of layers has to match `pool_res` number.

#### `pool_res INT [INT ...]`
Number (each number) and resolution (each number) of pooling layers. 

Default is `1140 780 580`.

Number of layers has to match `nfc` number.


#### `norm batch|instance|group`
Normalization to use: Batch, Instance or Group.

Default is `batch`.

#### `num_groups INT`
__Only needed if `norm group`__.

Number of groups.

Default is `16`.

#### `init_type normal|xavier|kaiming|orthogonal`
Type of network initialization.

Default is `normal`.

#### `init_gain FLOAT`
**Only needed if `init_type normal|xavier|orthogonal`**

Scaling factor for intialization.

Default is `0.02`.

#### `num_threads INT`

Number of threads for loading data.

Default is `3`.

#### `gpu_ids INT [INT ...]`

Specify GPU IDs, for CPU use `-1`.

Default is `0`.

#### `name NAME`
Name of the experiment, used to store samples and models.

Default is `debug`.

#### `checkpoints_dir PATH`
Models are saved in specified path.

Default is `./checkpoints`.

#### `serial_batches`
If present, meshes are loaded in order, otherwhise randomly.

#### `seed INT`
If present, uses specified seed.

#### `export folder PATH`
Export intermediate collapses to path.

Default is "` `".

#### `plus`
If present, use MeshCNNPlus, if not, use MeshCNN.

#### `csv`
If present, load data from CSV files.

## Training
---
#### `print_freq INT`
Frecuency of showing training results on console.

Default is `10`.

#### `save_latest_freq INT`
Frecuency of saving the latest results.

Default is `250`.

#### `save_epoc_freq INT`
Frecuency of saving checkpoints at end of epochs.

Default is `1`.

#### `run_test_freq INT`
Frecuency of running test in training script.

Default is `1`.

#### `continue_train`
If present, continues training from latest saved model.

#### `epoch_count INT`
Starting epoch count.

Default is `1`.

#### `which_epoch STR`
Which epoch to load?

Default is `latest`

#### `niter INT`
Number of epochs using the initial learning rate.

Default is `100`

#### `niter_decay INT`
Number of epochs to linearly decay learning rate to zero.

Default is `500`.

#### `beta1 FLOAT`
Momentum term of ADAM optimization.

Default is `0.9`.

#### `lr FLOAT`
Initial learning rate.

Default is `0.0002`.

#### `lr_policy lambda|step|plateau`
Learning rate policy

Default is `lambda`.

#### `lr_decay_iters INT`
Multiply by a gamma every lr_decay_iters

Default is `50`.

#### `num_aug INT`
Number of new augmented meshes to add.

Default is `10`.

#### `scale_verts`
If present, meshes are non-uniformly scaled.


#### `slide_verts FLOAT`
Percent vertices which will be shifted along the mesh surface

Default is `0`.

#### `flip_edges FLOAT`
Percent of edges to randomly flip.

Default is `0`.

#### `no_vis`
If present, will not use TensorBoard.

#### `verbose_plot`
If present, plots network weights.

#### `optimizer adam|sgd|rmsprop|adagrad`
What optimizer to use.

#### `amsgrad`
**Only needed if `optimizer adam`**
If present, use AMSGrad instead of ADAM.
self.parser.add_argument('--amsgrad', action='store_true', help='Use AMSGrad on ADAM')

Default is `adam`.

#### `validation`
If present, use validation.

#### `verbose_train`
If present, show more details of the training process.

## Testing
---
#### `results_dir STR`
Path to save the results

Default is `./results/`.

#### `which_epoch STR`
Epoch to load for testing.

Default is `latest`.

#### `veborse`
If present, testing shows Accuracy, Precision, Recall and F1.

#### `confusion_matrix`
If present, testing shows confusion matrix.