# Potato Leaf Disease Classification

## Setup for Python:

1. Install Python ([Setup instructions](https://wiki.python.org/moin/BeginnersGuide))

2. Install Python packages

```
pip3 install -r training/requirements.txt
pip3 install -r api/requirements.txt
```

3. Install Tensorflow Serving ([Setup instructions](https://www.tensorflow.org/tfx/serving/setup))

## Setup for ReactJS

1. Install Nodejs ([Setup instructions](https://nodejs.org/en/download/package-manager/))
2. Install NPM ([Setup instructions](https://www.npmjs.com/get-npm))
3. Install dependencies

```bash
cd frontend
npm install --from-lock-json
npm audit fix
```

4. Copy `.env.example` as `.env`.

5. Change API url in `.env`.

## Setup for React-Native app

1. Go to the [React Native environment setup](https://reactnative.dev/docs/environment-setup), then select `React Native CLI Quickstart` tab.  

2. Install dependencies

```bash
cd mobile-app
yarn install
```

  - 2.1 Only for mac users
```bash
cd ios && pod install && cd ../
```

3. Copy `.env.example` as `.env`.

4. Change API url in `.env`.

## Training the Model

1. Download the data from [kaggle](https://www.kaggle.com/arjuntejaswi/plant-village).
2. Only keep folders related to Potatoes.
3. Run Jupyter Notebook in Browser.

```bash
jupyter notebook
```

4. Open `training/potato-disease-classification-model.ipynb` in Jupyter Notebook.
5. In cell #2, update the path to dataset.
6. Run all the Cells one by one.
7. Copy the model generated and save it with the version number in the `models` folder.

## Running the API

### Using FastAPI

1. Get inside `api` folder

```bash
cd api
```

2. Run the FastAPI Server using uvicorn

```bash
uvicorn main:app --reload --host 0.0.0.0
```

3. Your API is now running at `0.0.0.0:8000`

### Using FastAPI 

1. Get inside `api` folder

```bash
cd api
```

2. Copy the `models.config.example` as `models.config` and update the paths in file.

3. Run the FastAPI Server using uvicorn
   For this you can directly run it from your main.py or main-tf-serving.py using pycharm run option (as shown in the video tutorial)
   OR you can run it from command prompt as shown below,

```bash
uvicorn main-tf-serving:app --reload --host 0.0.0.0
```

4. Your API is now running at `0.0.0.0:8000`

## Running the Frontend

1. Get inside `api` folder

```bash
cd frontend
```

2. Copy the `.env.example` as `.env` and update `REACT_APP_API_URL` to API URL if needed.
3. Run the frontend

```bash
npm run start
```

Here's the revised and well-organized version of your content:

## Mobile App Deployment - In Android Studio Emulator:

**1. Dependencies:**
It is recommended to use an LTS version of Node. If you want to be able to switch between different versions, you might want to install Node via nvm-windows, a Node version manager for Windows.

React Native also requires Java SE Development Kit (JDK), which can be installed using Chocolatey as well. Open an Administrator Command Prompt (right-click Command Prompt and select "Run as Administrator"), then run the following command:

```bash
choco install -y nodejs-lts microsoft-openjdk11
```

If you have already installed Node on your system, make sure it is Node 16 or newer. If you already have a JDK on your system, we recommend JDK 11. You may encounter problems using higher JDK versions.

**2. Upgrade Gradle:**
If you're using the latest version of the Java Development Kit, you'll need to change the Gradle version of your project so it can recognize the JDK. You can do that by going to `{project root folder}\android\gradle\wrapper\gradle-wrapper.properties` and changing the `distributionUrl` value to upgrade the Gradle version. You can check out the latest releases of Gradle [here](https://gradle.org/releases/).

**3. Android Development Environment Setup:**
Setting up your development environment can be somewhat tedious if you're new to Android development. If you're already familiar with Android development, there are a few things you may need to configure. In either case, please make sure to carefully follow the next few steps.

**4. Install Android Studio:**
Download and install Android Studio. While on the Android Studio installation wizard, make sure the boxes next to all of the following items are checked:

- Android SDK
- Android SDK Platform
- Android Virtual Device

If you are not already using Hyper-V: Performance (Intel ® HAXM) (See [here](https://developer.android.com/studio/run/emulator-acceleration) for AMD or Hyper-V). Then, click "Next" to install all of these components. If the checkboxes are grayed out, you will have a chance to install these components later on.

Once setup has finalized and you're presented with the Welcome screen, proceed to the next step.

**5. Install the Android SDK:**
Android Studio installs the latest Android SDK by default. Building a React Native app with native code, however, requires the Android 13 (Tiramisu) SDK in particular. Additional Android SDKs can be installed through the SDK Manager in Android Studio. To do that, open Android Studio, click on "More Actions" button and select "SDK Manager".

The SDK Manager can also be found within the Android Studio "Preferences" dialog, under Appearance & Behavior → System Settings → Android SDK.

Select the "SDK Platforms" tab from within the SDK Manager, then check the box next to "Show Package Details" in the bottom right corner. Look for and expand the Android 13 (Tiramisu) entry, then make sure the following items are checked:

- Android SDK Platform 33
- Intel x86 Atom_64 System Image or Google APIs Intel x86 Atom System Image

Next, select the "SDK Tools" tab and check the box next to "Show Package Details" here as well. Look for and expand the Android SDK Build-Tools entry, then make sure that 33.0.0 is selected. Finally, click "Apply" to download and install the Android SDK and related build tools.

**6. Configure the ANDROID_HOME Environment Variable:**
The React Native tools require some environment variables to be set up in order to build apps with native code. Open the Windows Control Panel. Click on User Accounts, then click User Accounts again. Click on Change my environment variables. Click on New... to create a new ANDROID_HOME user variable that points to the path to your Android SDK:

The SDK is installed, by default, at the following location:

```
%LOCALAPPDATA%\Android\Sdk
```

You can find the actual location of the SDK in the Android Studio "Settings" dialog, under Appearance & Behavior → System Settings → Android SDK.

Open a new Command Prompt window to ensure the new environment variable is loaded before proceeding to the next step. Open PowerShell and copy and paste `Get-ChildItem -Path Env:\` into PowerShell to verify that ANDROID_HOME has been added.

**7. Add platform-tools to Path:**
Open the Windows Control Panel. Click on User Accounts, then click User Accounts again. Click on Change my environment variables. Select the Path variable. Click Edit. Click New and add the path to platform-tools to the list. The default location for this folder is:

```
%LOCALAPPDATA%\Android\Sdk\platform-tools
```

**8. React Native Command Line Interface (CLI):**
React Native has a built-in command line interface. Rather than install and manage a specific version of the CLI globally, we recommend you access the current version at runtime using npx, which ships with Node.js. With `npx react-native <command>`, the current stable version of the CLI will be downloaded and executed at the time the command is run.

**9. Creating a New Application:**
Get inside the `mobile-app` folder:

```bash
cd mobile-app
```

Go to your project directory and run:

```bash
yarn global add [package-name]
yarn global add create-react-app
yarn install
```

**10. Configure Environment Variables:**
Copy the `.env.example` as `.env` and update the `URL` to the API URL if needed.

**11. Running the App:**
Run the app on Android or iOS:

```bash
npm run android
```

or

```bash
npm run ios
```

**12. Creating a Public Signed APK:**
After syncing the gradles in the Android Studio emulator, you will get the Metro Bundler. Make sure you run the Android Studio emulator beforehand. Finally, you can deploy the DL model into the mobile emulator through GCP invoking.


## Deploying the TF Model (.h5) on GCP

1. Create a [GCP account](https://console.cloud.google.com/freetrial/signup/tos?_ga=2.25841725.1677013893.1627213171-706917375.1627193643&_gac=1.124122488.1627227734.Cj0KCQjwl_SHBhCQARIsAFIFRVVUZFV7wUg-DVxSlsnlIwSGWxib-owC-s9k6rjWVaF4y7kp1aUv5eQaAj2kEALw_wcB).
2. Create a [Project on GCP](https://cloud.google.com/appengine/docs/standard/nodejs/building-app/creating-project) (Keep note of the project id).
3. Create a [GCP bucket](https://console.cloud.google.com/storage/browser/).
4. Upload the tf .h5 model generate in the bucket in the path `models/leaf_disease_dl_model.h5`.
5. Install Google Cloud SDK ([Setup instructions](https://cloud.google.com/sdk/docs/quickstarts)).
6. Authenticate with Google Cloud SDK.

```bash
gcloud auth login
```

7. Run the deployment script.

```bash
cd gcp
gcloud functions deploy predict --runtime python38 --trigger-http --memory 512 --project project_id
```

8. Your model is now deployed.
9. Use Postman to test the GCF using the [Trigger URL](https://cloud.google.com/functions/docs/calling/http).

Inspiration: https://cloud.google.com/blog/products/ai-machine-learning/how-to-serve-deep-learning-models-using-tensorflow-2-0-with-cloud-functions


## Incase of error or delay

1. Delete npm caches You can clear the npm cache by running the following command in your terminal:

```bash
npm cache clean --force

```

2. Run gradlew clean Navigate to your project directory where the gradlew file is located and run the following command:

```bash
gradlew clean (for windows)

```
3. Delete node_modules and package-lock.json: Still in your project directory, you can delete the node_modules directory and package-lock.json file with these commands:

```bash
rmdir /s /q node_modules

```

```bash
del /f package-lock.json

```

4. To reinstall all:

```bash
npm install

```