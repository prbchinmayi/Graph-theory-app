from __future__ import annotations

import builtins
import contextlib
import io
import runpy
import traceback
from dataclasses import dataclass
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import streamlit as st


BASE_DIR = Path(__file__).parent
EXPERIMENTS_DIR = BASE_DIR / "experiments"
THEORY_DIR = BASE_DIR / "theory"
AIMS_DIR = BASE_DIR / "aims"
CONCLUSIONS_DIR = BASE_DIR / "conclusions"
LOGO_PATH = BASE_DIR / "gec logo.jpg"


@dataclass(frozen=True)
class ExperimentPart:
    label: str
    filename: str
    method: str


@dataclass(frozen=True)
class Experiment:
    number: int
    title: str
    aim: str
    algorithm: list[str]
    expected_output: str
    viva: list[tuple[str, str]]
    parts: tuple[ExperimentPart, ...]


EXPERIMENTS: list[Experiment] = [
    Experiment(
        1,
        "Basic Graphs",
        "Aim will be added after the practical content is provided.",
        [
            "Import the required NetworkX and Matplotlib libraries.",
            "Create different graph types such as complete, cycle, path, and bipartite graphs.",
            "Assign suitable layouts to each graph.",
            "Draw the graphs with vertex labels and titles.",
            "Observe and compare the structure of the generated graphs."
        ],
        "Displays standard graph visualizations such as K5, C5, P5, and K2,3.",
        [
            ("What is a graph?", "A graph is a set of vertices connected by edges."),
            ("What is NetworkX used for?", "NetworkX is used to create, analyze, and visualize graphs in Python."),
        ],
        (
            ExperimentPart("With Inbuilt Functions", "exp1_with_inbuilt.py", "NetworkX"),
            ExperimentPart("Without Inbuilt Functions", "exp1_without_inbuilt.py", "Manual"),
        ),
    ),
    Experiment(
        2,
        "Isomorphism",
        "Aim will be added after the practical content is provided.",
        [
            "Construct the two graphs to be compared.",
            "Compare the number of vertices, edges, and degree sequences.",
            "Check structural properties such as adjacency and cycles.",
            "Determine a valid vertex mapping between the graphs.",
            "Report whether the graphs are isomorphic."
        ],
        "Prints graph invariants, mapping details, and isomorphism status with visual comparison.",
        [
            ("What is graph isomorphism?", "Two graphs are isomorphic if they have the same structure under vertex relabelling."),
            ("Why compare degree sequences?", "Different degree sequences prove that two graphs cannot be isomorphic."),
        ],
        (
            ExperimentPart("With Inbuilt Functions", "exp2_with_inbuilt.py", "NetworkX"),
            ExperimentPart("Without Inbuilt Functions", "exp2_without_inbuilt.py", "Manual"),
        ),
    ),
    Experiment(
        3,
        "Subgraphs",
        "Aim will be added after the practical content is provided.",
        [
            "Create the original graph.",
            "Select a subset of vertices or edges from the graph.",
            "Construct the corresponding subgraph.",
            "Compare the subgraph with the original graph.",
            "Display both graphs for analysis."
        ],
        "Shows whether the graph is connected and displays the graph structure.",
        [
            ("What is a connected graph?", "A graph is connected if every vertex is reachable from every other vertex."),
            ("Which traversals help test connectivity?", "Breadth-first search and depth-first search are commonly used."),
        ],
        (
            ExperimentPart("With Inbuilt Functions", "exp3_with_inbuilt.py", "NetworkX"),
            ExperimentPart("Without Inbuilt Functions", "exp3_without_inbuilt.py", "Manual"),
        ),
    ),
    Experiment(
        4,
        "Havel Hakiami Algorithm",
        "Aim will be added after the practical content is provided.",
        [
            "Input the degree sequence.",
            "Arrange the sequence in non-increasing order.",
            "Remove the largest degree and subtract one from the next corresponding degrees.",
            "Repeat the process until all degrees become zero or a negative value appears.",
            "Report whether the sequence is graphical."
        ],
        "Displays graph decision output and a supporting visualization.",
        [
            ("What is an Euler circuit?", "An Euler circuit uses every edge exactly once and returns to the start."),
            ("What is a Hamiltonian cycle?", "A Hamiltonian cycle visits every vertex exactly once and returns to the start."),
        ],
        (
            ExperimentPart("With Inbuilt Functions", "exp4_with_inbuilt.py", "NetworkX"),
            ExperimentPart("Without Inbuilt Functions", "exp4_without_inbuilt.py", "Manual"),
        ),
    ),
    Experiment(
        5,
        "Line Graphs",
        "Aim will be added after the practical content is provided.",
        [
            "Construct the original graph.",
            "Represent every edge of the original graph as a vertex in the line graph.",
            "Connect two vertices in the line graph if their corresponding edges share a common endpoint.",
            "Generate the line graph.",
            "Display both the original graph and its line graph."
        ],
        "Prints original graph edges, line graph vertices, line graph edges, and displays both graphs.",
        [
            ("What is a line graph?", "A line graph represents every edge of the original graph as a vertex."),
            ("When are two line-graph vertices adjacent?", "They are adjacent when the corresponding original edges share an endpoint."),
        ],
        (
            ExperimentPart("With Inbuilt Functions", "exp5_with_inbuilt.py", "NetworkX"),
            ExperimentPart("Without Inbuilt Functions", "exp5_without_inbuilt.py", "Manual"),
        ),
    ),
    Experiment(
        6,
        "Minimum Spanning Tree",
        "Aim will be added after the practical content is provided.",
        [
            "Create a connected weighted graph.",
            "Sort the edges according to their weights.",
            "Select the smallest edge that does not form a cycle.",
            "Repeat until all vertices are connected with n−1 edges.",
            "Display the Minimum Spanning Tree and its total weight."
        ],
        "Displays vertex colors, chromatic information, and a colored graph.",
        [
            ("What is graph coloring?", "Graph coloring assigns colors so adjacent vertices do not share the same color."),
            ("What is chromatic number?", "It is the minimum number of colors needed for a proper coloring."),
        ],
        (
            ExperimentPart("With Inbuilt Functions", "exp6_with_inbuilt.py", "NetworkX"),
            ExperimentPart("Without Inbuilt Functions", "exp6_without_inbuilt.py", "Manual"),
        ),
    ),
    Experiment(
        7,
        "Shortest Path Algorithm",
        "Aim will be added after the practical content is provided.",
        [
            "Construct a weighted graph.",
            "Select the source and destination vertices.",
            "Apply Dijkstra's shortest path algorithm.",
            "Compute the minimum distance and corresponding path.",
            "Display the shortest path and its total cost."
        ],
        "Prints shortest path information and shows the graph visualization.",
        [
            ("What is a shortest path?", "It is a path between two vertices with minimum total length or weight."),
            ("Which algorithm is common for weighted graphs?", "Dijkstra's algorithm is commonly used when weights are non-negative."),
        ],
        (
            ExperimentPart("With Inbuilt Functions", "exp7_with_inbuilt.py", "NetworkX"),
            ExperimentPart("Without Inbuilt Functions", "exp7_without_inbuilt.py", "Manual"),
        ),
    ),
    Experiment(
        8,
        "Walks, Trails and Paths",
        "Aim will be added after the practical content is provided.",
        [
            "Construct the original graph.",
            "Select a sequence of vertices and edges.",
            "Identify whether the sequence is a walk, trail, or path.",
            "Verify repeated vertices and repeated edges where applicable.",
            "Display and classify the obtained sequence."
        ],
        "Shows selected MST edges, total weight, and graph visualization.",
        [
            ("What is a spanning tree?", "It is a connected acyclic subgraph containing all vertices."),
            ("What is an MST?", "It is a spanning tree with minimum possible total edge weight."),
        ],
        (
            ExperimentPart("With Inbuilt Functions", "exp8_with_inbuilt.py", "NetworkX"),
            ExperimentPart("Without Inbuilt Functions", "exp8_without_inbuilt.py", "Manual"),
        ),
    ),
    Experiment(
        9,
        "Eularian Circuits",
        "Aim will be added after the practical content is provided.",
        [
            "Construct the graph.",
            "Check whether the graph is connected.",
            "Determine the degree of every vertex.",
            "Verify the conditions for an Eulerian circuit or path.",
            "Display the Eulerian circuit if it exists; otherwise report that none exists."
        ],
        "Prints whether the graph is planar and displays the related visualization.",
        [
            ("What is a planar graph?", "A planar graph can be drawn in a plane without crossing edges."),
            ("Name a non-planar graph.", "K5 and K3,3 are classic non-planar graphs."),
        ],
        (
            ExperimentPart("With Inbuilt Functions", "exp9_with_inbuilt.py", "NetworkX"),
            ExperimentPart("Without Inbuilt Functions", "exp9_without_inbuilt.py", "Manual"),
        ),
    ),
    Experiment(
        10,
        "Hamiltonian Cycles",
        "Aim will be added after the practical content is provided.",
        [
            "Construct the graph.",
            "Choose a starting vertex.",
            "Visit each vertex exactly once using backtracking.",
            "Check whether the last vertex connects back to the starting vertex.",
            "Display the Hamiltonian cycle if one exists."
        ],
        "Displays matching or covering results with a graph visualization.",
        [
            ("What is a matching?", "A matching is a set of edges with no shared endpoints."),
            ("What is a vertex cover?", "A vertex cover is a set of vertices touching every edge."),
        ],
        (
            ExperimentPart("With Inbuilt Functions", "exp10_with_inbuilt.py", "NetworkX"),
            ExperimentPart("Without Inbuilt Functions", "exp10_without_inbuilt.py", "Manual"),
        ),
    ),
    Experiment(
        11,
        "Vertex Colouring",
        "Aim will be added after the practical content is provided.",
        [
            "Construct the graph.",
            "Arrange the vertices in a suitable order.",
            "Assign the smallest available colour to each vertex without conflicting with adjacent vertices.",
            "Repeat until all vertices are coloured.",
            "Display the coloured graph and the chromatic number."
        ],
        "Shows vertex coloring applications such as Sudoku and vertex coloring visualizations.",
        [
            ("How is Sudoku related to graph coloring?", "Each cell is a vertex and constraints are edges between cells that cannot share values."),
            ("Why is graph coloring useful?", "It models scheduling, register allocation, map coloring, and puzzle constraints."),
        ],
        (
            ExperimentPart("Sudoku Coloring", "exp11_sudoku.py", "Application"),
            ExperimentPart("Vertex Coloring", "exp11_vertexcolouring.py", "Application"),
        ),
    ),
]


def configure_page() -> None:
    st.set_page_config(
        page_title="Graph Theory and Combinetrics Lab",
        page_icon="GT",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown(
        """
        <style>
        :root {
            --navy: #12324a;
            --ink: #1f2937;
            --line: #d9e2ec;
            --mint: #1f9d8a;
            --gold: #d99a22;
            --paper: #f7f9fc;
        }
        .stApp {
            background: #eef4f7;
            color: var(--ink);
            padding-top: 3.9rem;
            padding-bottom: 4rem;
        }
        .block-container {
            max-width: 1180px;
            padding-top: 5.2rem;
            padding-left: 2.4rem;
            padding-right: 2.4rem;
        }
        .stApp,
        .stApp p,
        .stApp label,
        .stMarkdown,
        .stMarkdown p,
        .stMarkdown li {
            color: var(--ink);
        }
        .stCaptionContainer,
        .stCaptionContainer p {
            color: #5f6f82 !important;
        }
        header[data-testid="stHeader"] { background: transparent; }
        section[data-testid="stSidebar"] {
            background: #ffffff;
            border-right: 1px solid var(--line);
        }
        section[data-testid="stSidebar"] * {
            color: var(--ink) !important;
        }
        section[data-testid="stSidebar"] .stRadio {
            background: #f8fbfd;
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 8px 10px;
        }
        .fixed-header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 999;
            min-height: 54px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 18px;
            padding: 7px 28px;
            background: rgba(255, 255, 255, 0.98);
            border-bottom: 1px solid var(--line);
            box-shadow: 0 10px 28px rgba(18, 50, 74, 0.08);
        }
        .brand-lockup {
            display: flex;
            align-items: center;
            gap: 14px;
            min-width: 0;
        }
        .brand-logo {
            width: 40px;
            height: 40px;
            object-fit: contain;
        }
        .brand-title {
            margin: 0;
            color: var(--navy);
            font-size: clamp(1.05rem, 2vw, 1.55rem);
            font-weight: 800;
            line-height: 1.08;
        }
        .brand-subtitle {
            margin: 1px 0 0;
            color: #667085;
            font-size: 0.78rem;
        }
        .header-pill {
            border: 1px solid var(--line);
            background: #f8fbfd;
            color: var(--navy);
            border-radius: 999px;
            padding: 6px 11px;
            font-size: 0.78rem;
            white-space: nowrap;
        }
        .fixed-footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            z-index: 999;
            display: flex;
            justify-content: center;
            gap: 16px;
            flex-wrap: wrap;
            padding: 10px 18px;
            background: rgba(18, 50, 74, 0.97);
            color: #ffffff;
            font-size: 0.9rem;
            border-top: 3px solid var(--gold);
        }
        .fixed-footer,
        .fixed-footer span {
            color: #ffffff !important;
        }
        .hero {
            border: 1px solid var(--line);
            background: #ffffff;
            border-radius: 8px;
            padding: clamp(18px, 3vw, 30px);
            box-shadow: 0 16px 40px rgba(18, 50, 74, 0.08);
        }
        .hero h1 {
            color: var(--navy);
            font-size: clamp(2rem, 4.8vw, 4.1rem);
            line-height: 1.02;
            margin: 0 0 10px;
            letter-spacing: 0;
        }
        .hero p {
            color: #536171;
            max-width: 860px;
            font-size: 1.02rem;
            line-height: 1.65;
            margin-bottom: 0;
        }
        .metric-row {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
            gap: 12px;
            margin: 18px 0 8px;
        }
        .metric-tile {
            border: 1px solid var(--line);
            border-left: 4px solid var(--mint);
            background: #ffffff;
            border-radius: 8px;
            padding: 14px 16px;
        }
        .metric-value {
            color: var(--navy);
            font-size: 1.5rem;
            font-weight: 800;
        }
        .metric-label {
            color: #667085;
            font-size: 0.86rem;
        }
        .section-panel {
            border: 1px solid var(--line);
            background: #ffffff;
            border-radius: 8px;
            padding: 18px;
            margin-top: 12px;
        }
        .section-panel h3 {
            margin-top: 0;
            color: var(--navy);
        }
        .part-badge {
            display: inline-flex;
            align-items: center;
            margin: 0 8px 8px 0;
            padding: 6px 10px;
            border: 1px solid #c8d7e1;
            border-radius: 999px;
            background: #f7fbfc;
            color: #23435a;
            font-size: 0.85rem;
        }
        .small-muted { color: #667085; font-size: 0.92rem; }
        .experiment-shell {
            background: #ffffff;
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: clamp(16px, 2.4vw, 28px);
            box-shadow: 0 18px 44px rgba(18, 50, 74, 0.07);
        }
        .experiment-shell h2 {
            color: var(--navy);
            font-size: clamp(1.8rem, 3.4vw, 2.7rem);
            line-height: 1.1;
            margin-bottom: 0.35rem;
        }
        .stRadio [role="radiogroup"] {
            gap: 14px;
        }
        .stRadio label {
            color: var(--ink) !important;
            font-weight: 600;
        }
        .stRadio label span {
            color: var(--ink) !important;
        }
        .stRadio [data-baseweb="radio"] {
            background: #ffffff;
            border: 1px solid #cbd8e3;
            border-radius: 999px;
            padding: 9px 13px;
            min-height: 42px;
        }
        .stRadio [data-baseweb="radio"]:has(input:checked) {
            border-color: #0f766e;
            background: #e9f7f4;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            border-bottom: 1px solid var(--line);
            margin-top: 14px;
        }
        .stTabs [data-baseweb="tab"] {
            background: #f8fbfd;
            border: 1px solid var(--line);
            border-bottom: 0;
            border-radius: 8px 8px 0 0;
            padding: 10px 14px;
            height: auto;
        }
        .stTabs [data-baseweb="tab"] p,
        .stTabs [data-baseweb="tab"] span {
            color: #34495e !important;
            font-weight: 700;
        }
        .stTabs [aria-selected="true"] {
            background: #ffffff;
            border-color: #0f766e;
            box-shadow: inset 0 -3px 0 #0f766e;
        }
        .stTabs [aria-selected="true"] p,
        .stTabs [aria-selected="true"] span {
            color: #0f766e !important;
        }
        div[data-testid="stExpander"] {
            border: 1px solid #cbd8e3;
            border-radius: 8px;
            background: #ffffff;
            overflow: hidden;
            margin-bottom: 10px;
        }
        div[data-testid="stExpander"] details summary {
            background: #f8fbfd;
            min-height: 48px;
        }
        div[data-testid="stExpander"] details summary,
        div[data-testid="stExpander"] details summary * {
            color: var(--ink) !important;
            font-weight: 700;
        }
        div[data-testid="stExpander"] details[open] summary {
            background: #e9f7f4;
            border-bottom: 1px solid #cbd8e3;
        }
        div[data-testid="stAlert"] {
            border-radius: 8px;
        }
        textarea,
        input {
            color: var(--ink) !important;
        }
        div[data-testid="stCodeBlock"] {
            border: 1px solid var(--line);
            border-radius: 8px;
        }
        .stButton > button {
            border-radius: 8px;
            border: 1px solid #0f766e;
            background: #0f766e;
            color: white;
            font-weight: 700;
            min-height: 2.7rem;
        }
        .stButton > button:hover {
            border-color: #115e59;
            background: #115e59;
            color: white;
        }
        @media (max-width: 720px) {
            .fixed-header {
                align-items: flex-start;
                padding: 10px 14px;
            }
            .brand-logo { width: 36px; height: 36px; }
            .header-pill { display: none; }
            .stApp { padding-top: 4.2rem; }
            .block-container {
                padding-top: 5.8rem;
                padding-left: 1rem;
                padding-right: 1rem;
            }
            .stTabs [data-baseweb="tab-list"] {
                overflow-x: auto;
                flex-wrap: nowrap;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_chrome() -> None:
    logo_html = ""
    if LOGO_PATH.exists():
        import base64

        encoded = base64.b64encode(LOGO_PATH.read_bytes()).decode("utf-8")
        logo_html = f'<img class="brand-logo" src="data:image/jpeg;base64,{encoded}" alt="GEC logo">'

    st.markdown(
        f"""
        <div class="fixed-header">
            <div class="brand-lockup">
                {logo_html}
                <div>
                    <h1 class="brand-title">Goa College of Engineering</h1>
                    <p class="brand-subtitle">Academic Year: 2025-2026 | CMP-225: Graph Theory and Combinatorics Laboratory</p>
                </div>
            </div>
            <div class="header-pill">Semester 4 Practical Course</div>
        </div>
        <div class="fixed-footer">
            <span>Chinmayi Parab</span>
            <span>|</span>
            <span>Rollno: 24B-CO-013</span>
            <span>|</span>
            <span>Semester 4</span>
            <br>
        </div>
        """,
        unsafe_allow_html=True,
    )


def load_source(filename: str) -> str:
    path = EXPERIMENTS_DIR / filename
    if not path.exists():
        return f"# Missing experiment file: {filename}"
    return path.read_text(encoding="utf-8", errors="replace")


def load_theory(experiment_number: int) -> str:
    path = THEORY_DIR / f"exp{experiment_number}.md"
    if path.exists():
        return path.read_text(encoding="utf-8", errors="replace")
    return (
        "Theory content will be added here after the final 300-500 word material "
        "is provided for this experiment."
    )


def load_aim(experiment: Experiment) -> str:
    path = AIMS_DIR / f"exp{experiment.number}.md"
    if path.exists():
        return path.read_text(encoding="utf-8", errors="replace")
    return experiment.aim


def load_conclusion(experiment_number: int) -> str:
    path = CONCLUSIONS_DIR / f"exp{experiment_number}.md"
    if path.exists():
        return path.read_text(encoding="utf-8", errors="replace")
    return (
        "Conclusion will be added here after the final practical observations "
        "and learning outcome are provided for this experiment."
    )


def needs_stdin(source: str) -> bool:
    return "input(" in source or "input (" in source


def sample_stdin(filename: str) -> str:
    if filename.startswith("exp5_"):
        return "4\n0 1 1 0\n1 0 1 1\n1 1 0 1\n0 1 1 0"
    return ""


def run_experiment(filename: str, stdin_text: str = "") -> dict[str, object]:
    source_path = EXPERIMENTS_DIR / filename
    stdout = io.StringIO()
    figures = []
    error = None
    original_input = builtins.input
    input_stream = io.StringIO(stdin_text)

    def streamlit_input(prompt: str = "") -> str:
        if prompt:
            print(prompt, end="")
        line = input_stream.readline()
        if line == "":
            raise RuntimeError("The experiment requested more input than the dashboard received.")
        return line.rstrip("\n")

    try:
        plt.close("all")
        builtins.input = streamlit_input
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stdout):
            runpy.run_path(str(source_path), run_name="__main__")
        figures = [plt.figure(num) for num in plt.get_fignums()]
    except Exception:
        error = traceback.format_exc()
        figures = [plt.figure(num) for num in plt.get_fignums()]
    finally:
        builtins.input = original_input

    return {
        "stdout": stdout.getvalue(),
        "figures": figures,
        "error": error,
    }


def experiment_by_number(number: int) -> Experiment:
    return next(exp for exp in EXPERIMENTS if exp.number == number)


def render_home(filtered: list[Experiment]) -> None:
    st.markdown(
        """
        <div class="hero">
            <h1>NetworkX Graph Theory Laboratory</h1>
            <p>
                A professional Streamlit virtual laboratory for graph theory and combinatorics practicals.
                Select an experiment from the sidebar, study the theory and algorithm, inspect the source
                code dynamically from the Python file, execute it, and view text output with Matplotlib
                or NetworkX visualizations inside the dashboard.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="metric-row">
            <div class="metric-tile"><div class="metric-value">{len(EXPERIMENTS)}</div><div class="metric-label">Experiments</div></div>
            <div class="metric-tile"><div class="metric-value">22</div><div class="metric-label">Python Programs</div></div>
            <div class="metric-tile"><div class="metric-value">6</div><div class="metric-label">Learning Tabs</div></div>
            <div class="metric-tile"><div class="metric-value">Live</div><div class="metric-label">Execution and Graphs</div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Experiment Selection Panel")
    cols = st.columns(2)
    for index, exp in enumerate(filtered):
        with cols[index % 2]:
            st.markdown(
                f"""
                <div class="section-panel">
                    <h3>Experiment {exp.number}: {exp.title}</h3>
                    <p class="small-muted">{exp.expected_output}</p>
                    {''.join(f'<span class="part-badge">{part.label}</span>' for part in exp.parts)}
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_experiment(exp: Experiment) -> None:
    st.markdown(f"## Experiment {exp.number}: {exp.title}")
    st.caption("Choose a part, review the learning material, run the program, and inspect the generated output.")

    part_labels = [part.label for part in exp.parts]
    selected_part_label = st.radio(
        "Experiment Part",
        part_labels,
        index=0,
        horizontal=True,
        label_visibility="collapsed",
    )
    part = next(p for p in exp.parts if p.label == selected_part_label)
    source = load_source(part.filename)
    result_key = f"result_exp{exp.number}_{part.filename}"

    theory_tab, algorithm_tab, source_tab, output_tab = st.tabs(
        ["Theory", "Algorithm", "Source Code", "Output"]
    )

    with theory_tab:
        st.markdown("### Aim")
        st.info(load_aim(exp))
        st.markdown("### Theory")
        st.markdown(load_theory(exp.number))
        st.markdown("### Conclusion")
        st.success(load_conclusion(exp.number))

    with algorithm_tab:
        st.markdown("### Algorithm")
        for index, step in enumerate(exp.algorithm, start=1):
            st.markdown(f"{index}. {step}")

    with source_tab:
        st.markdown(f"### Source Code Viewer: `{part.filename}`")
        st.code(source, language="python", line_numbers=True)
        stdin_text = ""
        if needs_stdin(source):
            stdin_text = st.text_area(
                "Program Input",
                value=sample_stdin(part.filename),
                height=150,
                help="Each line is passed to Python input() in order.",
            )
        if st.button("Run Experiment", key=f"run_{exp.number}_{part.filename}", use_container_width=True):
            st.session_state[result_key] = run_experiment(part.filename, stdin_text)
            st.success("Experiment executed. Open the Output tab to view text and visualizations.")

    with output_tab:
        st.markdown("### Output")
        result = st.session_state.get(result_key)
        if not result:
            st.info("Run the experiment from the Execution tab to generate output.")
        else:
            text_output = str(result.get("stdout") or "").strip()
            error_output = result.get("error")
            figures = result.get("figures") or []

            st.markdown("#### Text Output")
            if text_output:
                st.code(text_output, language="text")
            else:
                st.caption("No text was printed by this experiment.")

            if error_output:
                st.markdown("#### Execution Error")
                st.error("The program stopped with an error.")
                st.code(str(error_output), language="text")

            st.markdown("#### Visualization Area")
            if figures:
                for fig_index, fig in enumerate(figures, start=1):
                    st.pyplot(fig, clear_figure=False, use_container_width=True)
                    st.caption(f"Figure {fig_index}")
            else:
                st.caption("No Matplotlib or NetworkX figure was produced.")

            st.markdown("#### Expected Output")
            st.write(exp.expected_output)

def render_sidebar() -> int:
    with st.sidebar:
        st.markdown("## Virtual Lab")
        search = st.text_input("Search Experiment", placeholder="Search by number, title, or topic")

        filtered = [
            exp
            for exp in EXPERIMENTS
            if not search
            or search.lower() in f"experiment {exp.number} {exp.title}".lower()
            or any(search.lower() in part.filename.lower() for part in exp.parts)
        ]

        st.markdown("### Experiments")
        visible_experiments = filtered or EXPERIMENTS
        options = {f"Experiment {exp.number}": exp.number for exp in visible_experiments}
        selected_label = st.radio(
            "Experiment List",
            list(options.keys()),
            label_visibility="collapsed",
        )
        selected_number = options[selected_label]

        if search and not filtered:
            st.warning("No experiments match the search text.")

        st.markdown("---")
        st.caption("Use the dashboard tabs for theory, algorithm, source code, and output.")

    return selected_number


def main() -> None:
    configure_page()
    render_chrome()
    selected_number = render_sidebar()
    render_experiment(experiment_by_number(selected_number or 1))


if __name__ == "__main__":
    main()
