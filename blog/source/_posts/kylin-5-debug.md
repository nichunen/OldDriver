---
title: How to setup debugging environment for Kylin5 locally
author: 倪春恩
img: /source/images/kylin_logo.png
top: false
hide: false
cover: true
coverImg: /images/kylin_logo.png
toc: false
categories: bigdata
tags:
  - kylin
date: 2023-01-31 16:44:33
---

### 1. Check Software Requirement

| Software     | Comment                                     | Version                                  | Download Link                                                |
| ------------ | ------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------ |
| Git          | Fetch branch name and hash of latest commit | latest                                   | https://git-scm.com/book/en/v2/Getting-Started-Installing-Git |
| Apache Maven | Build Java and Scala source code            | 3.8.2 or latest                          | https://maven.apache.org/download.cgi                        |
| Node.js      | Build front end                             | 12.14.0 is recommended ( or 12.x ~ 14.x) | [How to switch to older node.js](https://kylin.apache.org/5.0/docs/development/how_to_package#install_older_node) |
| JDK          | Java Compiler and Development Tools         | JDK 1.8.x                                | https://www.oracle.com/java/technologies/javase/javase8u211-later-archive-downloads.html |

After installing the above software, please verify **software requirements** by following commands:

```shell
$ java -version
$ mvn -v
$ node -v
$ git version
```

**Options for Packaging Script**

| Option        | Comment                                                      |
| ------------- | ------------------------------------------------------------ |
| -official     | If adding this option, the package name won't contain the timestamp |
| -noThirdParty | If adding this option, third-party binary won't be packaged into binary, current they are influxdb,grafana and PostgreSQL |
| -noSpark      | If adding this option, spark won't be packaged into the Kylin binary |
| -noHive1      | By default Kylin 5.0 will support Hive 1.2, if add this option, this binary will support Hive 2.3+ |
| -skipFront    | If add this option, the front-end won't be built and packaged |
| -skipCompile  | Add this option will assume java source code no need to be compiled again |

**Other Options for Packaging Script**

| Option     | Comment                                                      |
| ---------- | ------------------------------------------------------------ |
| -P hadoop3 | Packaging a Kylin 5.0 software package for running on Hadoop 3.0 + platform. |

**Package Content**

| Option      | Comment                           |
| ----------- | --------------------------------- |
| VERSION     | `Apache Kylin ${release_version}` |
| commit_SHA1 | `${HASH_COMMIT}@${BRANCH_NAME}`   |

**Package Name convention**

Package name is `apache-kylin-${release_version}.tar.gz`, while `${release_version}` is `{project.version}.YYYYmmDDHHMMSS` by default. For example, an unofficial package could be `apache-kylin-5.0.0-SNAPSHOT.20220812161045.tar.gz` while an official package could be `apache-kylin-5.0.0.tar.gz`

**Example for developer and release manager**

```shell
## Case 1: For the developer who wants to package for testing purposes
./build/release/release.sh 

## Case 2: Official apache release,  Kylin binary for deployment on Hadoop3+ and Hive2.3+, 
# and the third party cannot be distributed because of apache distribution policy(size and license)
./build/release/release.sh -noSpark -official 

## Case 3: A package for Apache Hadoop 3 platform
./build/release/release.sh -P hadoop3
```



### 2. Build source code

+ Clone

  ```shell
  git clone https://github.com/apache/kylin.git
  cd kylin
  git checkout kylin5
  ```

- Build backend source code before your start debugging.

  ```shell
  mvn clean install -DskipTests
  ```

- Build front-end source code.

  (Please use node.js **v12.14.0**, for how to use a specific version of node.js, please check [how to switch to a specific node js](https://kylin.apache.org/5.0/docs/development/how_to_package#install_older_node) )

  ```shell
  cd kystudio
  npm install
  ```



### 3. Install IntelliJ IDEA and build the source

1. Install the IDEA Community edition (the Ultimate edition is ok too).
2. Import the source code into IDEA. Click the **Open**, and choose the directory of **Kylin source code**. ![img](https://kylin.apache.org/5.0/assets/images/OPEN_KYLIN_PROJECT-99e9296de444a46f0c3f2cc63881edea.png)

3. Install the scala plugin and restart

![image-20230208213032938](C:\Users\zhudanchen\AppData\Roaming\Typora\typora-user-images\image-20230208213032938.png)

4. Configure SDK(JDK and Scala), make sure you use **JDK 1.8.X** and **Scala 2.12.X**.

   ![image-20230208214536615](C:\Users\zhudanchen\AppData\Roaming\Typora\typora-user-images\image-20230208214536615.png)

5. Reload maven projects, and the `scala` directory will be marked as source root(in blue color).

   ![image-20230208214558630](C:\Users\zhudanchen\AppData\Roaming\Typora\typora-user-images\image-20230208214558630.png)

6. Build the projects.(make sure you have executed `mvn clean package -DskipTests`, otherwise some source code is not generated by maven javacc plugin)

   ![image-20230208214731367](C:\Users\zhudanchen\AppData\Roaming\Typora\typora-user-images\image-20230208214731367.png)
