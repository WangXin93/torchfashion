from nose.tools import *
from utils.datasets import FashionAttrsDataset, image_datasets, dataloaders

def setup_tests():
    print('SETUP!')


def datasets_tests():
    csv_file =  '/home/wangx/datasets/fashionAI/web/Annotations/skirt_length_labels_train.csv'
    root_dir = '/home/wangx/datasets/fashionAI/web/'
    
    # Test FashionAttrsDataset
    fashion_dataset = FashionAttrsDataset(csv_file, root_dir)
    assert_true(len(fashion_dataset)>0)

    # Test image_datasets
    for _, image_dataset in image_datasets.items():
        assert_true(len(image_dataset) > 0)

    # Test dataloaders
    for _, dataloader in dataloaders.items():
        next_batch = next(iter(dataloader))
        assert_true(list(next_batch['image'].shape), [32, 2, 224, 224])

