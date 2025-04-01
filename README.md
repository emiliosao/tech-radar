# Blackbirds Tech Radar

Blackbirds Tech Radar is a simple, self-hosted tool to visualize technology adoption across different categories. This project is based on the Zalando Tech Radar and has been customized for Blackbirds.ai.

## Getting Started

### Prerequisites
- Python 3
- A local web server (such as Python's built-in HTTP server)

### Running Locally
1. Clone the repository:
   ```sh
   git clone https://github.com/emiliosao/tech-radar.git
   cd tech-radar
   ```
2. Start a local web server:
   ```sh
   python3 -m http.server 8000
   ```
3. Open your browser and visit:
   ```
   http://localhost:8000
   ```

## Updating the Radar

### Modifying Entries
- Update `tech-radar.xlsx` with new or modified entries.
- Run the update script to regenerate `config.json`:
  ```sh
  python3 excel_to_json.py
  ```
- Refresh the page to see the updated radar.

## Customizing the Style
- Modify `index.html` to change visual elements such as colors, fonts, and layout.
- `radar.css` controls the main styles of the radar visualization.
   - Styles can also be overriden in `radar.js` by commenting out the lines at the beginning of the `radar_visualization` function.

## Notes
This radar was designed for [Blackbirds.ai](https://www.blackbirds.ai/), but it can be adapted and hosted anywhere.

