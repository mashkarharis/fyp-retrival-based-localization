# Steps
steps = [9]

# Building Params
x_lim=60
y_lim=150
# x_lim=15
# y_lim=40
# Root Dir
root_dir = "C:\\Users\\mashk\\MyFiles\\Semester 8\\FYP\\code\\project_implementation\\outputs\\3. set - through-ronin-custom-contrastive"

# Step1: Generate CSV From HDF5
hdf5datadir = {
    "db": {
        "loc": f"{root_dir}\\nilocdata-subset\\unib\\seen",
        "isseen": True,
        "countperset": -1,
        "indb": True
    },
    "train": {
        "loc": f"{root_dir}\\nilocdata-subset\\unib\\seen",
        "isseen": True,
        "countperset": 16,
        "indb": False
    },
    "test": {
        "loc": f"{root_dir}\\nilocdata-subset\\unib\\unseen",
        "isseen": False,
        "countperset": 2,
        "indb": False
    },
    "val": {
        "loc": f"{root_dir}\\nilocdata-subset\\unib\\unseen",
        "isseen": False,
        "countperset": 2,
        "indb": False

    }

}
csv_out_dir = f"{root_dir}\\1. csv_data"
preferred_files = {
    'loc': 'computed/aligned_pos',
    'gyro': "synced/gyro",
    'acce': "synced/acce",
    'game_rv': "synced/game_rv"
}

# Step2: Generate Train/Test/Val From HDF5
freq = 200  # Dpoints Per Sec
no_of_sec_per_split = 45  # Windows Size
train_test_val_meta_file = f"{root_dir}\\train_test_val_meta.csv"

# Step3: Get RoNIN Trajectory
sample_rate=freq
ronin_checkpoint = f"{root_dir}\\ronin_resnet\\checkpoint_gsn_latest.pt"
processed_hdf5_out_dir = f"{root_dir}\\2. processed_data"

# Step4 : Draw Trajectory
traj_drawing_out_dir = f"{root_dir}\\3. traj_visualized"

# Step5 : Make Time Invariant
invariant_domain_output_dir = f"{root_dir}\\4. invariant"
segment_length = 0.1

# Step6 : Image DB Generate
image_db_loc = f"{root_dir}\\5. imageDB"
image_db_meta_file = f"{root_dir}\\image_db_meta_file.csv"
window_size = 120  # Same Length Curve For All Images : Length = 220 x 0.1 = 22
step_size = 50

# Step7 : Build KDTree
image_db_loc_kdtree = f"{root_dir}\\5. imageDB\\db"
kdtree_features_loc = f"{root_dir}\\kdtree_features.pickle"
kdtree_tags_loc = f"{root_dir}\\kdtree_tags.pickle"
frechet_distance_threshold=10

# Step8 : Eval Tune
train_invariant_dir = f"{root_dir}\\4. invariant\\train"
test_invariant_dir = f"{root_dir}\\4. invariant\\test"
val_invariant_dir = f"{root_dir}\\4. invariant\\val"
extracted_data_output_loc=f"{root_dir}\\6. Extracted Data"
no_of_candidates=50

# Step9 : History Model
to_eval_dir = f"{root_dir}\\4. invariant\\train"
history_output_loc=f"{root_dir}\\7. History"
db_meta_csv = image_db_meta_file
invariant_dir = invariant_domain_output_dir
filter_distance_threshold=10
max_no_of_frames = 4