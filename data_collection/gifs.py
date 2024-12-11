import pyvibms
import os
import pymol
from pymol import cmd
from PIL import Image

# Define function to visualize vibrations and save as GIFs
def visualize_vibrations_with_gifs(hess_file, output_dir, fps=30):
    """
    Analyze vibrational modes from a .hess file and save movies in GIF format.

    Parameters:
    - hess_file (str): Path to the .hess file.
    - output_dir (str): Directory to save GIFs.
    - fps (int): Frames per second for the GIFs.
    """
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load vibrational data
    print("Loading Hessian file...")
    vib_data = pyvibms.load_hessian(hess_file)

    # Analyze vibrational modes
    print("Analyzing vibrational modes...")
    modes = vib_data.analyze_vibrations()

    for i, mode in enumerate(modes):
        print(f"Creating GIF for mode {i + 1}/{len(modes)}...")

        # Generate PyMOL object for the vibrational mode
        structure = vib_data.get_structure()
        vibrations = vib_data.get_mode_vibrations(mode, scale=1.0)

        # Save structure to a temporary file
        pdb_file = os.path.join(output_dir, f"mode_{i + 1}.pdb")
        structure.write_pdb(pdb_file)

        # Load structure into PyMOL
        cmd.reinitialize()
        cmd.load(pdb_file, "molecule")

        # Generate frames for the vibration
        frame_files = []
        for frame_idx, frame in enumerate(vibrations):
            frame_file = os.path.join(output_dir, f"mode_{i + 1}_frame_{frame_idx:03d}.png")
            cmd.frame(frame)
            cmd.png(frame_file, width=800, height=600, dpi=300, ray=True)
            frame_files.append(frame_file)

        # Generate GIF from frames
        gif_path = os.path.join(output_dir, f"mode_{i + 1}.gif")
        images = [Image.open(frame) for frame in frame_files]
        images[0].save(gif_path, save_all=True, append_images=images[1:], duration=int(1000 / fps), loop=0)

        # Clean up frame files
        for frame_file in frame_files:
            os.remove(frame_file)

    print(f"GIFs saved to {output_dir}")

# Main function
if __name__ == "__main__":
    # Input .hess file path
    hess_file = "example.hess"  # Replace with your .hess file path

    # Output directory
    output_dir = "vibrational_gifs"

    # Visualize vibrations and save as GIFs
    visualize_vibrations_with_gifs(hess_file, output_dir)
