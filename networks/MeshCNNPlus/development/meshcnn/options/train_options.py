from .base_options import BaseOptions

class TrainOptions(BaseOptions):
    def initialize(self):
        BaseOptions.initialize(self)
        self.parser.add_argument('--print_freq', type=int, default=1000, help='frequency of showing training results on console')
        self.parser.add_argument('--save_latest_freq', type=int, default=250, help='frequency of saving the latest results')
        self.parser.add_argument('--save_epoch_freq', type=int, default=1, help='frequency of saving checkpoints at the end of epochs')
        self.parser.add_argument('--run_test_freq', type=int, default=1, help='frequency of running test in training script')
        self.parser.add_argument('--continue_train', action='store_true', help='continue training: load the latest model')
        self.parser.add_argument('--epoch_count', type=int, default=1, help='the starting epoch count, we save the model by <epoch_count>, <epoch_count>+<save_latest_freq>, ...')
        self.parser.add_argument('--phase', type=str, default='train', help='train, val, test, etc')
        self.parser.add_argument('--which_epoch', type=str, default='latest', help='which epoch to load? set to latest to use latest cached model')
        self.parser.add_argument('--niter', type=int, default=100, help='# of iter at starting learning rate')
        self.parser.add_argument('--niter_decay', type=int, default=500, help='# of iter to linearly decay learning rate to zero')
        self.parser.add_argument('--beta1', type=float, default=0.9, help='momentum term of adam')
        self.parser.add_argument('--lr', type=float, default=0.0002, help='initial learning rate for adam')
        self.parser.add_argument('--lr_policy', type=str, default='lambda', help='learning rate policy: lambda|step|plateau')
        self.parser.add_argument('--lr_decay_iters', type=int, default=50, help='multiply by a gamma every lr_decay_iters iterations')

        # data augmentation stuff
        self.parser.add_argument('--num_aug', type=int, default=10, help='# of augmentation files')
        self.parser.add_argument('--scale_verts', action='store_true', help='non-uniformly scale the mesh e.g., in x, y or z')
        self.parser.add_argument('--slide_verts', type=float, default=0, help='percent vertices which will be shifted along the mesh surface')
        self.parser.add_argument('--flip_edges', type=float, default=0, help='percent of edges to randomly flip')
        # tensorboard visualization
        self.parser.add_argument('--no_vis', action='store_true', help='will not use tensorboard')
        self.parser.add_argument('--verbose_plot', action='store_true', help='plots network weights, etc.')

        # - Dropout can be added now.
        #self.parser.add_argument("--dropout", type=float, default=0, help='Percentage of DropOut to use on every hidden FC layer')
        self.parser.add_argument('--dropout',nargs='+', type=float, default=[0], help='Percentage of DropOut to use on every hidden FC layer')

        # - AMSGrad can be set from here now.
        self.parser.add_argument('--amsgrad', action='store_true', help='Use AMSGrad on ADAM')
        # - Optimizers
        self.parser.add_argument('--optimizer', type=str, default='adam', help='Optimizers: adam|sgd|rmsprop|adagrad')
        # - Validation
        self.parser.add_argument('--validation', action='store_true')
        # - Show Training (and optinally, Validation) Accuracy and Loss
        self.parser.add_argument('--verbose_train', action='store_true')

        self.is_train = True
