from argparse import ArgumentParser

import cv2

from optical_flow_algo import dense_optical_flow
from optical_flow_algo import lucas_kanade_method

'''
python first_approach.py --algorithm rlof --video_path image.mp4
python first_approach.py --algorithm farneback --video_path image.mp4
python first_approach.py --algorithm lucaskanade --video_path image.mp4
python first_approach.py --algorithm lucaskanade_dense --video_path image.mp4
'''
def main():
    parser = ArgumentParser()
    parser.add_argument(
        "--algorithm",
        choices=["farneback", "lucaskanade", "lucaskanade_dense", "rlof"],
        required=True,
        help="Optical flow algorithm to use",
    )
    parser.add_argument(
        "--video_path", default="videos/cat.mp4", help="Path to the video",
    )

    args = parser.parse_args()
    video_path = args.video_path
    if args.algorithm == "lucaskanade":
        lucas_kanade_method(video_path)
    elif args.algorithm == "lucaskanade_dense":
        method = cv2.optflow.calcOpticalFlowSparseToDense
        dense_optical_flow(method, video_path, to_gray=True)
    elif args.algorithm == "farneback":
        method = cv2.calcOpticalFlowFarneback
        params = [0.5, 3, 15, 3, 5, 1.2, 0]  # Farneback's algorithm parameters
        dense_optical_flow(method, video_path, params, to_gray=True)
    elif args.algorithm == "rlof":
        method = cv2.optflow.calcOpticalFlowDenseRLOF
        dense_optical_flow(method, video_path)


if __name__ == "__main__":
    main()



