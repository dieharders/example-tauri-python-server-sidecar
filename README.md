# Example Tauri App using a Python server

A native web-app using the Tauri framework that spawns a subprocess for a backend server (FastAPI).

---

## Introduction

This is a hybrid Next.js + Python app that uses Next.js as the frontend and FastAPI as the API backend.

It is intended to show how to build hybrid language apps that work locally on a client's computer.

We do this to package up dependencies to make installation easier on the user and to allow the front-end access to the OS's disk, camera, and other native hardware features.

We make use of PyInstaller to compile binaries of all our code so that the user doesn't have to worry about installing dependencies. Tauri accomplishes this interoperability with what it calls "sidecars" which you can use to "load" in some arbitrary runtime. This is defined in the `tauri.conf.json` file. See [here](https://tauri.app/v1/guides/building/sidecar/) for more info.

Unfortunately this is done through Rust which some (including myself) are not familiar. Therefore, after many a visit to StackOverflow I created this example project in case others or myself ever need to jump-start a new native app.

---

## How It Works

- Tauri takes your front-end UI written in javascript (or Next.js framework in this case) and creates a native webview to display it. This makes the file size much smaller.

- In `main.rs` we spawn a `main.py` script which creates our api server on `localhost:8008` and can be used to spawn any other binaries or python code you like.

- Most importantly, when the user closes the GUI window, all processes and subprocesses are shutdown properly.

- 3rd party client apps could use this api to perform any functions needed. Use it to run ai inference, offload intensive tasks, manually kick-off or orchestrate processes.

---

## Getting Started

### Dependencies

First, install the dependencies for javascript:

```bash
pnpm install
```

Install dependencies for python listed in your requirements.txt file:

Be sure to run this command with admin privileges. This command is optional and is also run on each `pnpm dev`.

```
pip install -r requirements.txt
```

### Run

Then, run the app in development mode:

```bash
pnpm tauri dev
```

---

### Build

In case you dont have PyInstaller installed:

```
pip install -U pyinstaller
```

A note on compiling Python exe (the -F flag bundles everything into one .exe). You won't need to run this manually each build, I have included it in the build scripts.

- `pyinstaller -c -F your_program.py`

Build app for production:

```
pnpm tauri build
```

This creates an installer located here:

- \<project-dir>\src-tauri\target\release\bundle\nsis

---

## Learn More

- [Tauri Framework](https://tauri.app/) - learn about native app development in javascript and rust.
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - learn about FastAPI features and API.
- [PyInstaller](https://pyinstaller.org/en/stable/) - learn about packaging python code.
