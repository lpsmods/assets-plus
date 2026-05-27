// Just configuration for Minecraft Bedrock Resource Pack
import { parallel, series, task } from "just-scripts";
import {
  cleanTask,
  cleanCollateralTask,
  copyTask,
  setupEnvironment,
  STANDARD_CLEAN_PATHS,
  DEFAULT_CLEAN_DIRECTORIES,
  getOrThrowFromProcess,
  watchTask,
  CopyTaskParameters,
  mcaddonTask,
} from "@minecraft/core-build-tasks";
import path from "path";
import fs from "fs";
import JSON5 from "json5";

function getManifestVersion(): string {
  const manifestPath = path.resolve(__dirname, `./resource_packs/${projectName}/manifest.json`);
  const manifest = JSON5.parse(fs.readFileSync(manifestPath, "utf8"));
  const version = manifest.header?.version;
  if (!version) {
    throw new Error(`Missing header.version in ${manifestPath}`);
  }
  return version;
}

setupEnvironment(path.resolve(__dirname, ".env"));
const projectName = getOrThrowFromProcess("PROJECT_NAME");
const projectVersion = getManifestVersion();

const resourcePackPath = `./resource_packs/${projectName}`;

const copyTaskOptions: CopyTaskParameters = {
  copyToResourcePacks: [resourcePackPath],
  copyToBehaviorPacks: [],
  copyToScripts: [],
};

// Build
task("build", copyTask(copyTaskOptions));

// Clean
task("clean-local", cleanTask(DEFAULT_CLEAN_DIRECTORIES));
task("clean-collateral", cleanCollateralTask(STANDARD_CLEAN_PATHS));
task("clean", parallel("clean-local", "clean-collateral"));

// Package only the resource pack as .mcpack
mcaddonTask({
  outputFile: `./dist/packages/${projectName}-${projectVersion}.mcaddon`,
  copyToResourcePacks: [`./resource_packs/${projectName}`],
  copyToBehaviorPacks: [],
  copyToScripts: [],
});

// Only run resource-pack packaging
task("mcpack", series("clean-local", "packRP"));

// Local Deploy
task(
  "local-deploy",
  watchTask(["resource_packs/**/*.{json,lang,png,tga,jpg,jpeg,ogg,wav}"], series("clean-local", "build")),
);
