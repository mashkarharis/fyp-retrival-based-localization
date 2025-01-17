from Configurations.Config import Config
from DBManager.DBManager import DBManager
from DBManager.eval import Evaluator
from compile_dataset.compiler import Compiler
from csv_converter.csv_generator import CSV_Generator
from domain_mapper.convert_domain import DomainConverter
from train_test_val.train_test_val import TrainTestValSplitter
from traj_visualizer.traj_visualizer import TrajVisualizer
from history.HistoryModel import HistoryModel
from history.DataStorer import DataStorer
from history.LSTM import LSTM
from floor_plan_builder.FingerPrintManager import FingerPrintManager

root_dir = "C:\\Users\\musab\\OneDrive\\Desktop\\projects\\fyp\\fyp-retrival-based-localization\\project_implementation\\outputs\\building_unib"
config = Config(root_dir)
steps = config.steps

if __name__ == "__main__":

    print("============================================\nTRAINER: RUN ONCE PER BUILDING\n============================================\nUpdate Following Configs According To Building\n------------------------\n1. Run\n\t- steps : steps to run\n\n2. Dataset to Train\n\t- root dir : root directory\n\t- hdf5datadir : db/train/test/val directory\n\n3. Generate Train Test Val Data\n\t- freq : capturing frequency of data [Hz][*]\n\t- no_of_sec_per_split : window size sufficient for capturing unique motion in the building, used for random cropping for train/test/val [s][*]\n\n4. Generate RoNIN Trajectories\n\t- ronin_checkpoint : where to find pretrained RoNIN ResNET Model\n\n5. Make Time Invariant\n\t- segment_length : segment length for resampling after interpolation [m][*]\n\n6. ImageDB Generate\n\t- window_size : no of segments per curve, sufficient to identify unique motion in the building, caputured for single image [*]\n\t- step_size : no of segments to skip for next image [*]\n\n8. Evaluation\n\t- no_of_candidates : run serveral times and identify how many candidates needed for best accuracy [*]\n\n[m] : Measured in Meters\n[Hz] : Measured in Hz\n[s] : Measured in Seconds\n[*] : Tune/Change According to Dataset\n============================================\n\n")

    if 1 in steps:
        csv_generator = CSV_Generator(config)
        csv_generator.generate()

    if 2 in steps:
        fmgr = FingerPrintManager(config)
        fmgr.build()


    if 3 in steps:
        splitter = TrainTestValSplitter(config)
        splitter.split()

    if 4 in steps:
        data_compiler = Compiler(config)
        data_compiler.compile()

    if 5 in steps:
        traj_visualizer = TrajVisualizer(config)
        traj_visualizer.drawRoNINTraj()

    if 6 in steps:
        domain_convertor = DomainConverter(config)
        domain_convertor.make_time_invariant()

    if 7 in steps:
        generate_imagedb = DBManager(config)
        generate_imagedb.generateImageDB()

    if 8 in steps:
        generate_imagedb = DBManager(config)
        generate_imagedb.buildKDTree()

    if 9 in steps:
        evaluator = Evaluator(config)
        evaluator.evaluate()

    config.save_config_to_json()
