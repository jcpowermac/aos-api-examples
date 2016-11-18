# Pods -> Containers 


Pod and containers

```yaml
apiVersion: v1
items:
- metadata:
    annotations:
      openshift.io/build.name: cakephp-mysql-example-1
      openshift.io/scc: privileged
    creationTimestamp: 2016-11-18T14:44:51Z
    labels:
      openshift.io/build.name: cakephp-mysql-example-1
    name: cakephp-mysql-example-1-build
    namespace: cake
    resourceVersion: "807380"
    selfLink: /api/v1/namespaces/cake/pods/cakephp-mysql-example-1-build
    uid: 8fcb7915-ad9d-11e6-a162-5254005823d9
  spec:
    containers:
    - args:
      - --loglevel=0
      env:
      - name: BUILD
        value: |
          {"kind":"Build","apiVersion":"v1","metadata":{"name":"cakephp-mysql-example-1","namespace":"cake","selfLink":"/oapi/v1/namespaces/cake/builds/cakephp-mysql-example-1","uid":"8fb6886a-ad9d-11e6-a162-5254005823d9","resourceVersion":"807272","creationTimestamp":"2016-11-18T14:44:51Z","labels":{"app":"cakephp-mysql-example","buildconfig":"cakephp-mysql-example","openshift.io/build-config.name":"cakephp-mysql-example","openshift.io/build.start-policy":"Serial","template":"cakephp-mysql-example"},"annotations":{"openshift.io/build-config.name":"cakephp-mysql-example","openshift.io/build.number":"1"}},"spec":{"serviceAccount":"builder","source":{"type":"Git","git":{"uri":"https://github.com/openshift/cakephp-ex.git"}},"strategy":{"type":"Source","sourceStrategy":{"from":{"kind":"DockerImage","name":"registry.access.redhat.com/rhscl/php-56-rhel7@sha256:743108b04515500100a0b3d170f23474fadb7ed94497d5556e48691f931bb619"},"env":[{"name":"COMPOSER_MIRROR"}]}},"output":{"to":{"kind":"DockerImage","name":"172.30.26.210:5000/cake/cakephp-mysql-example:latest"},"pushSecret":{"name":"builder-dockercfg-adcio"}},"resources":{},"postCommit":{},"triggeredBy":[{"message":"Build configuration change"}]},"status":{"phase":"New","outputDockerImageReference":"172.30.26.210:5000/cake/cakephp-mysql-example:latest","config":{"kind":"BuildConfig","namespace":"cake","name":"cakephp-mysql-example"}}}
      - name: SOURCE_REPOSITORY
        value: https://github.com/openshift/cakephp-ex.git
      - name: SOURCE_URI
        value: https://github.com/openshift/cakephp-ex.git
      - name: ORIGIN_VERSION
        value: v3.3.0.35
      - name: ALLOWED_UIDS
        value: 1-
      - name: DROP_CAPS
        value: KILL,MKNOD,SETGID,SETUID,SYS_CHROOT
      - name: PUSH_DOCKERCFG_PATH
        value: /var/run/secrets/openshift.io/push
      image: openshift3/ose-sti-builder:v3.3.0.35
      imagePullPolicy: IfNotPresent
      name: sti-build
      resources: {}
      securityContext:
        privileged: true
      terminationMessagePath: /dev/termination-log
      volumeMounts:
      - mountPath: /var/run/docker.sock
        name: docker-socket
      - mountPath: /var/run/secrets/openshift.io/push
        name: builder-dockercfg-adcio-push
        readOnly: true
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: builder-token-o7oyz
        readOnly: true
    dnsPolicy: ClusterFirst
    host: origin-node2.virtomation.com
    imagePullSecrets:
    - name: builder-dockercfg-adcio
    nodeName: origin-node2.virtomation.com
    nodeSelector:
      region: primary
    restartPolicy: Never
    securityContext: {}
    serviceAccount: builder
    serviceAccountName: builder
    terminationGracePeriodSeconds: 30
    volumes:
    - hostPath:
        path: /var/run/docker.sock
      name: docker-socket
    - name: builder-dockercfg-adcio-push
      secret:
        secretName: builder-dockercfg-adcio
    - name: builder-token-o7oyz
      secret:
        secretName: builder-token-o7oyz
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: 2016-11-18T14:44:51Z
      reason: PodCompleted
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: 2016-11-18T14:46:39Z
      reason: PodCompleted
      status: "False"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: 2016-11-18T14:44:51Z
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://146d1ad0979d372efd3070c89eb37d541b21fe00b3f01d29b6dee5cce586e06b
      image: openshift3/ose-sti-builder:v3.3.0.35
      imageID: docker://sha256:7c04adeca203a36b3ff1415cee15869b516f5deac9367c514feeff4df7000ab8
      lastState: {}
      name: sti-build
      ready: false
      restartCount: 0
      state:
        terminated:
          containerID: docker://146d1ad0979d372efd3070c89eb37d541b21fe00b3f01d29b6dee5cce586e06b
          exitCode: 0
          finishedAt: 2016-11-18T14:46:38Z
          reason: Completed
          startedAt: 2016-11-18T14:44:58Z
    hostIP: 10.53.252.52
    phase: Succeeded
    podIP: 10.1.2.4
    startTime: 2016-11-18T14:44:51Z
- metadata:
    annotations:
      kubernetes.io/created-by: |
        {"kind":"SerializedReference","apiVersion":"v1","reference":{"kind":"ReplicationController","namespace":"cake","name":"cakephp-mysql-example-1","uid":"cfcd7732-ad9d-11e6-a162-5254005823d9","apiVersion":"v1","resourceVersion":"807404"}}
      openshift.io/deployment-config.latest-version: "1"
      openshift.io/deployment-config.name: cakephp-mysql-example
      openshift.io/deployment.name: cakephp-mysql-example-1
      openshift.io/scc: restricted
    creationTimestamp: 2016-11-18T14:46:54Z
    generateName: cakephp-mysql-example-1-
    labels:
      deployment: cakephp-mysql-example-1
      deploymentconfig: cakephp-mysql-example
      name: cakephp-mysql-example
    name: cakephp-mysql-example-1-squtq
    namespace: cake
    resourceVersion: "807423"
    selfLink: /api/v1/namespaces/cake/pods/cakephp-mysql-example-1-squtq
    uid: d8e4850b-ad9d-11e6-a162-5254005823d9
  spec:
    containers:
    - env:
      - name: DATABASE_SERVICE_NAME
        value: mysql
      - name: DATABASE_ENGINE
        value: mysql
      - name: DATABASE_NAME
        value: default
      - name: DATABASE_USER
        value: cakephp
      - name: DATABASE_PASSWORD
        value: x3wRTc0KfxPFeaOl
      - name: CAKEPHP_SECRET_TOKEN
        value: Ce7jsqKkwKWkzXzeFNsVIH81XWZQMbC7FRf3XFN7P2aFSj_4qR
      - name: CAKEPHP_SECURITY_SALT
        value: 52g7aLOaAfePsjE7xiu6Fd5aE8JhNgOantP37uVY
      - name: CAKEPHP_SECURITY_CIPHER_SEED
        value: "344276385624142148473800455543"
      - name: OPCACHE_REVALIDATE_FREQ
        value: "2"
      image: 172.30.26.210:5000/cake/cakephp-mysql-example@sha256:e0897c87cbe1248cd0da790f33dbf12cf6340de02b2c2d0fcea6a9a191135ca3
      imagePullPolicy: IfNotPresent
      livenessProbe:
        failureThreshold: 3
        httpGet:
          path: /
          port: 8080
          scheme: HTTP
        initialDelaySeconds: 30
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 3
      name: cakephp-mysql-example
      ports:
      - containerPort: 8080
        protocol: TCP
      readinessProbe:
        failureThreshold: 3
        httpGet:
          path: /health.php
          port: 8080
          scheme: HTTP
        initialDelaySeconds: 3
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 3
      resources:
        limits:
          memory: 512Mi
        requests:
          memory: 512Mi
      securityContext:
        capabilities:
          drop:
          - KILL
          - MKNOD
          - SETGID
          - SETUID
          - SYS_CHROOT
        privileged: false
        runAsUser: 1000510000
        seLinuxOptions:
          level: s0:c23,c2
      terminationMessagePath: /dev/termination-log
      volumeMounts:
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: default-token-o9d88
        readOnly: true
    dnsPolicy: ClusterFirst
    host: origin-node2.virtomation.com
    imagePullSecrets:
    - name: default-dockercfg-efxyd
    nodeName: origin-node2.virtomation.com
    nodeSelector:
      region: primary
    restartPolicy: Always
    securityContext:
      fsGroup: 1000510000
      seLinuxOptions:
        level: s0:c23,c2
    serviceAccount: default
    serviceAccountName: default
    terminationGracePeriodSeconds: 30
    volumes:
    - name: default-token-o9d88
      secret:
        secretName: default-token-o9d88
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: 2016-11-18T14:46:54Z
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: 2016-11-18T14:47:04Z
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: 2016-11-18T14:46:54Z
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://97c618303b729c32ab725e2f69f7cf2270809511f88a4349a130fa4b45eaf10f
      image: 172.30.26.210:5000/cake/cakephp-mysql-example@sha256:e0897c87cbe1248cd0da790f33dbf12cf6340de02b2c2d0fcea6a9a191135ca3
      imageID: docker://sha256:2fff35c7190b54a128807edf41d57f06722840497bb05e0353d2eb49978711ff
      lastState: {}
      name: cakephp-mysql-example
      ready: true
      restartCount: 0
      state:
        running:
          startedAt: 2016-11-18T14:46:59Z
    hostIP: 10.53.252.52
    phase: Running
    podIP: 10.1.2.4
    startTime: 2016-11-18T14:46:54Z
- metadata:
    annotations:
      kubernetes.io/created-by: |
        {"kind":"SerializedReference","apiVersion":"v1","reference":{"kind":"ReplicationController","namespace":"cake","name":"mysql-1","uid":"8fba2369-ad9d-11e6-a162-5254005823d9","apiVersion":"v1","resourceVersion":"807301"}}
      openshift.io/deployment-config.latest-version: "1"
      openshift.io/deployment-config.name: mysql
      openshift.io/deployment.name: mysql-1
      openshift.io/scc: restricted
    creationTimestamp: 2016-11-18T14:44:59Z
    generateName: mysql-1-
    labels:
      deployment: mysql-1
      deploymentconfig: mysql
      name: mysql
    name: mysql-1-zoe9j
    namespace: cake
    resourceVersion: "807331"
    selfLink: /api/v1/namespaces/cake/pods/mysql-1-zoe9j
    uid: 9464939a-ad9d-11e6-a162-5254005823d9
  spec:
    containers:
    - env:
      - name: MYSQL_USER
        value: cakephp
      - name: MYSQL_PASSWORD
        value: x3wRTc0KfxPFeaOl
      - name: MYSQL_DATABASE
        value: default
      image: registry.access.redhat.com/rhscl/mysql-56-rhel7@sha256:0a710d858de8752b70c4fbebb7c157050549a0cfc1b2e52301a20990648d02a7
      imagePullPolicy: IfNotPresent
      livenessProbe:
        failureThreshold: 3
        initialDelaySeconds: 30
        periodSeconds: 10
        successThreshold: 1
        tcpSocket:
          port: 3306
        timeoutSeconds: 1
      name: mysql
      ports:
      - containerPort: 3306
        protocol: TCP
      readinessProbe:
        exec:
          command:
          - /bin/sh
          - -i
          - -c
          - MYSQL_PWD='x3wRTc0KfxPFeaOl' mysql -h 127.0.0.1 -u cakephp -D default
            -e 'SELECT 1'
        failureThreshold: 3
        initialDelaySeconds: 5
        periodSeconds: 10
        successThreshold: 1
        timeoutSeconds: 1
      resources:
        limits:
          memory: 512Mi
        requests:
          memory: 512Mi
      securityContext:
        capabilities:
          drop:
          - KILL
          - MKNOD
          - SETGID
          - SETUID
          - SYS_CHROOT
        privileged: false
        runAsUser: 1000510000
        seLinuxOptions:
          level: s0:c23,c2
      terminationMessagePath: /dev/termination-log
      volumeMounts:
      - mountPath: /var/lib/mysql/data
        name: data
      - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: default-token-o9d88
        readOnly: true
    dnsPolicy: ClusterFirst
    host: origin-node1.virtomation.com
    imagePullSecrets:
    - name: default-dockercfg-efxyd
    nodeName: origin-node1.virtomation.com
    nodeSelector:
      region: primary
    restartPolicy: Always
    securityContext:
      fsGroup: 1000510000
      seLinuxOptions:
        level: s0:c23,c2
    serviceAccount: default
    serviceAccountName: default
    terminationGracePeriodSeconds: 30
    volumes:
    - emptyDir: {}
      name: data
    - name: default-token-o9d88
      secret:
        secretName: default-token-o9d88
  status:
    conditions:
    - lastProbeTime: null
      lastTransitionTime: 2016-11-18T14:44:59Z
      status: "True"
      type: Initialized
    - lastProbeTime: null
      lastTransitionTime: 2016-11-18T14:45:29Z
      status: "True"
      type: Ready
    - lastProbeTime: null
      lastTransitionTime: 2016-11-18T14:44:59Z
      status: "True"
      type: PodScheduled
    containerStatuses:
    - containerID: docker://cfadd2c4cb5c606462444eff37ff0c186c57c3116221c502d1290a38e7e8c513
      image: registry.access.redhat.com/rhscl/mysql-56-rhel7@sha256:0a710d858de8752b70c4fbebb7c157050549a0cfc1b2e52301a20990648d02a7
      imageID: docker://sha256:a3f541704bd2b1bdabd8f00bebc0ead3a7dd71f3b2bb1ee4e9afaddb7a62ba60
      lastState: {}
      name: mysql
      ready: true
      restartCount: 0
      state:
        running:
          startedAt: 2016-11-18T14:45:05Z
    hostIP: 10.53.252.51
    phase: Running
    podIP: 10.1.0.4
    startTime: 2016-11-18T14:44:59Z
kind: PodList
metadata:
  resourceVersion: "815296"
  selfLink: /api/v1/namespaces/cake/pods
```
