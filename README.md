# Circle CI Introspection

This REPO exists to fingerprint functionality implemented in CircleCI so that we can identify ways to write more usefull features for `astropy/nbcollection`


## Environment Varibles available on CI Build

### main branch commit

This ENVVar Name/Value dump was created by pushing a commit to the `main` branch
```
CI true
CIRCLECI true
CIRCLE_BRANCH main
CIRCLE_BUILD_NUM 3
CIRCLE_BUILD_URL https://circleci.com/gh/jbcurtin/circle-ci-instrospection/3
CIRCLE_JOB Echo ENVVars
CIRCLE_NODE_INDEX 0
CIRCLE_NODE_TOTAL 1
CIRCLE_PR_NUMBER None
CIRCLE_PR_REPONAME None
CIRCLE_PR_USERNAME None
CIRCLE_PREVIOUS_BUILD_NUM 2
CIRCLE_PROJECT_REPONAME circle-ci-instrospection
CIRCLE_PROJECT_USERNAME jbcurtin
CIRCLE_PULL_REQUEST None
CIRCLE_PULL_REQUESTS None
CIRCLE_REPOSITORY_URL git@github.com:jbcurtin/circle-ci-instrospection.git
CIRCLE_SHA1 c3b7766761f639ca2f3c0df188af4257c7326c3f
CIRCLE_TAG None
CIRCLE_USERNAME jbcurtin
CIRCLE_WORKFLOW_ID 4f7238f8-bbeb-4428-912f-da28c816002f
CIRCLE_WORKING_DIRECTORY ~/repo
CIRCLE_INTERNAL_TASK_DATA /.circleci-task-data
CIRCLE_COMPARE_URL 
CI_PULL_REQUEST None
CI_PULL_REQUESTS None
```

### PR Commit

This ENVVar Name/Value dump was created by pushing a commit to the `main` branch in 
`jbcurtin-shadow/circle-ci-introspection`, then a PR was opened to merged the fork back into
`jbcurtin/circle-ci-introspection`

```
CI true
CIRCLECI true
CIRCLE_BRANCH pull/1
CIRCLE_BUILD_NUM 5
CIRCLE_BUILD_URL https://circleci.com/gh/jbcurtin/circle-ci-instrospection/5
CIRCLE_JOB Echo ENVVars
CIRCLE_NODE_INDEX 0
CIRCLE_NODE_TOTAL 1
CIRCLE_PR_NUMBER 1
CIRCLE_PR_REPONAME circle-ci-instrospection
CIRCLE_PR_USERNAME jbcurtin-shadow
CIRCLE_PREVIOUS_BUILD_NUM 
CIRCLE_PROJECT_REPONAME circle-ci-instrospection
CIRCLE_PROJECT_USERNAME jbcurtin
CIRCLE_PULL_REQUEST https://github.com/jbcurtin/circle-ci-instrospection/pull/1
CIRCLE_PULL_REQUESTS https://github.com/jbcurtin/circle-ci-instrospection/pull/1
CIRCLE_REPOSITORY_URL git@github.com:jbcurtin/circle-ci-instrospection.git
CIRCLE_SHA1 7a4ece73befc72d3e7cbc4682cd652d10bf097b8
CIRCLE_TAG None
CIRCLE_USERNAME 
CIRCLE_WORKFLOW_ID f9a9cff4-f89c-41f8-94f1-b7b94df2ca75
CIRCLE_WORKING_DIRECTORY ~/repo
CIRCLE_INTERNAL_TASK_DATA /.circleci-task-data
CIRCLE_COMPARE_URL 
CI_PULL_REQUEST https://github.com/jbcurtin/circle-ci-instrospection/pull/1
CI_PULL_REQUESTS https://github.com/jbcurtin/circle-ci-instrospection/pull/1
```
