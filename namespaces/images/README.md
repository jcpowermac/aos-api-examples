# ImageStreamImage - Layers


The Dockerfile doesn't need to run just build so we can see the layers.


```json
{
   "kind":"ImageStreamImage",
   "image":{
      "dockerImageManifestMediaType":"application/vnd.docker.distribution.manifest.v1+json",
      "dockerImageMetadataVersion":"1.0",
      "dockerImageLayers":[
         {
            "mediaType":"application/vnd.docker.container.image.rootfs.diff+x-gtar",
            "name":"sha256:30cf2e26a24f2a8426cbe8444f8af2ecb7023bd468b05c1b6fd0b2797b0f9ff9",
            "size":71250133
         },
         {
            "mediaType":"application/vnd.docker.container.image.rootfs.diff+x-gtar",
            "name":"sha256:99dd41655d8a45c2fb74f9eeb73e327b3ad4796f0ff0d602c575e32e9804baed",
            "size":700
         },
         {
            "mediaType":"application/vnd.docker.container.image.rootfs.diff+x-gtar",
            "name":"sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4",
            "size":32
         },
         {
            "mediaType":"application/vnd.docker.container.image.rootfs.diff+x-gtar",
            "name":"sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4",
            "size":32
         },
         {
            "mediaType":"application/vnd.docker.container.image.rootfs.diff+x-gtar",
            "name":"sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4",
            "size":32
         },
         {
            "mediaType":"application/vnd.docker.container.image.rootfs.diff+x-gtar",
            "name":"sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4",
            "size":32
         },
         {
            "mediaType":"application/vnd.docker.container.image.rootfs.diff+x-gtar",
            "name":"sha256:52475c50f12ea89a35b9c535c33223bcec1c8ac6f2326b6ce40e66543c6420f7",
            "size":62673417
         },
         {
            "mediaType":"application/vnd.docker.container.image.rootfs.diff+x-gtar",
            "name":"sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4",
            "size":32
         },
         {
            "mediaType":"application/vnd.docker.container.image.rootfs.diff+x-gtar",
            "name":"sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4",
            "size":32
         },
         {
            "mediaType":"application/vnd.docker.container.image.rootfs.diff+x-gtar",
            "name":"sha256:cf151f0888ff3c55088d7a0a2055770b1fdf7c12e2f28c47a08b5a439a5b75f0",
            "size":8139
         },
         {
            "mediaType":"application/vnd.docker.container.image.rootfs.diff+x-gtar",
            "name":"sha256:9d69a49feb31efd204fceb773142f57cc0c70146b006b000732e33db9beb796a",
            "size":164
         },
         {
            "mediaType":"application/vnd.docker.container.image.rootfs.diff+x-gtar",
            "name":"sha256:12a8eb1bc110880943f886844f1b041ec3ddaece6e4d5b0e59331ded5629ada6",
            "size":533
         },
         {
            "mediaType":"application/vnd.docker.container.image.rootfs.diff+x-gtar",
            "name":"sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4",
            "size":32
         },
         {
            "mediaType":"application/vnd.docker.container.image.rootfs.diff+x-gtar",
            "name":"sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4",
            "size":32
         },
         {
            "mediaType":"application/vnd.docker.container.image.rootfs.diff+x-gtar",
            "name":"sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4",
            "size":32
         },
         {
            "mediaType":"application/vnd.docker.container.image.rootfs.diff+x-gtar",
            "name":"sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4",
            "size":32
         },
         {
            "mediaType":"application/vnd.docker.container.image.rootfs.diff+x-gtar",
            "name":"sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4",
            "size":32
         },
         {
            "mediaType":"application/vnd.docker.container.image.rootfs.diff+x-gtar",
            "name":"sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4",
            "size":32
         }
      ],
      "metadata":{
         "annotations":{
            "openshift.io/image.managed":"true"
         },
         "resourceVersion":"739841",
         "creationTimestamp":"2016-11-16T14:54:56Z",
         "name":"sha256:664c4f8b0939942f72ade86ab830db7cc1b68fcecbbec2b6b4d7db1a66c48805",
         "uid":"a35f35f4-ac0c-11e6-a162-5254005823d9"
      },
      "dockerImageReference":"172.30.26.210:5000/testing/mysql-container@sha256:664c4f8b0939942f72ade86ab830db7cc1b68fcecbbec2b6b4d7db1a66c48805",
      "dockerImageSignatures":[
         "eyJoZWFkZXIiOnsiandrIjp7ImNydiI6IlAtMjU2Iiwia2lkIjoiUExGMjpLWVBWOkE3WkE6VTJEVzpXN0ZPOkJMQUY6TU9RNzpFUktZOkhHREM6U1ZOWjpERU9EOlQ1WUwiLCJrdHkiOiJFQyIsIngiOiJTTnZoa1gxWWtmUkEyazdsRWlzRHpNRjlCZXl6eXo3Nm1wNlRHNDg2enNBIiwieSI6ImxJRFJFZWFUR2wxSWVTSEwxMDA1ZmpERmpZMDQtNjlsSWJTanlGN01hbEUifSwiYWxnIjoiRVMyNTYifSwic2lnbmF0dXJlIjoiczdBeV9nYUh0SFZSRk43d0NLWG5BaTdjMjVjQmNEZl94NXV0WDBRVUU2V0hQMHNXWFlaRlRtc1M0WV81NEE5YTdUUDB6SkdRNWpKb2syNWtQSzBBbFEiLCJwcm90ZWN0ZWQiOiJleUptYjNKdFlYUk1aVzVuZEdnaU9qRTFNakU0TENKbWIzSnRZWFJVWVdsc0lqb2lRMjR3SWl3aWRHbHRaU0k2SWpJd01UWXRNVEV0TVRaVU1UUTZOVFE2TlRaYUluMCJ9"
      ],
      "dockerImageMetadata":{
         "kind":"DockerImage",
         "Container":"d69d8d473e5cef6ec9731034da94eb7b39731274022ca91da4d57b6f2f775434",
         "DockerVersion":"1.10.3",
         "Parent":"5387079fe16f1477c4dbe71091fbeaaf3bb0b6fc5bbda31009f37f17f5a43763",
         "Created":"2016-11-16T14:54:53Z",
         "apiVersion":"1.0",
         "Architecture":"amd64",
         "ContainerConfig":{
            "Hostname":"d69d8d473e5c",
            "Volumes":{
               "/var/lib/mysql/data":{

               }
            },
            "Image":"sha256:2d2ac08e0333cc3150f7eef388e6b172ed7d31a7ad8d47509b0af73697b7ef3e",
            "Cmd":[
               "/bin/sh",
               "-c",
               "#(nop) LABEL io.openshift.build.commit.author=Joseph Callen \\\\u003cjcpowermac@gmail.com\\\\u003e io.openshift.build.commit.date=Tue Nov 8 16:50:52 2016 -0500 io.openshift.build.commit.id=a4043f50f66cd3fd30feb178bc7b680f358ff61a io.openshift.build.commit.ref=master io.openshift.build.commit.message=Changes to support utf8 io.openshift.build.source-location=https://github.com/jcpowermac/mysql-container io.openshift.build.source-context-dir=5.6"
            ],
            "Labels":{
               "io.k8s.description":"MySQL is a multi-user, multi-threaded SQL database server",
               "io.openshift.build.commit.author":"Joseph Callen \\\\u003cjcpowermac@gmail.com\\\\u003e",
               "io.openshift.build.commit.message":"Changes to support utf8",
               "Version":"5.6",
               "vcs-ref":"08780b7a7779335cf28f64654e43c75ad9341c77",
               "Vendor":"Red Hat, Inc.",
               "io.k8s.display-name":"MySQL 5.6",
               "io.openshift.build.source-context-dir":"5.6",
               "io.openshift.build.commit.date":"Tue Nov 8 16:50:52 2016 -0500",
               "Authoritative_Registry":"registry.access.redhat.com",
               "distribution-scope":"public",
               "Name":"rhscl/mysql-56-rhel7",
               "Build_Host":"rcm-img-docker02.build.eng.bos.redhat.com",
               "io.openshift.build.commit.ref":"master",
               "vcs-type":"git",
               "Architecture":"x86_64",
               "Release":"1",
               "BZComponent":"rh-mysql56-docker",
               "build-date":"2016-09-06T14:12:54.553894Z",
               "io.openshift.build.source-location":"https://github.com/jcpowermac/mysql-container",
               "summary":"MySQL is a multi-user, multi-threaded SQL database server",
               "architecture":"x86_64",
               "io.openshift.build.commit.id":"a4043f50f66cd3fd30feb178bc7b680f358ff61a",
               "release":"104",
               "io.openshift.expose-services":"3306:mysql",
               "io.openshift.tags":"database,mysql,mysql56,rh-mysql56",
               "com.redhat.build-host":"rcm-img-docker02.build.eng.bos.redhat.com"
            },
            "ExposedPorts":{
               "3306/tcp":{

               }
            },
            "User":"27",
            "Env":[
               "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
               "container=docker",
               "MYSQL_VERSION=5.6",
               "HOME=/var/lib/mysql",
               "CONTAINER_SCRIPTS_PATH=/usr/share/container-scripts/mysql",
               "MYSQL_PREFIX=/opt/rh/rh-mysql56/root/usr",
               "ENABLED_COLLECTIONS=rh-mysql56",
               "BASH_ENV=/usr/share/container-scripts/mysql/scl_enable",
               "ENV=/usr/share/container-scripts/mysql/scl_enable",
               "PROMPT_COMMAND=. /usr/share/container-scripts/mysql/scl_enable",
               "OPENSHIFT_BUILD_NAME=mysql-container-1",
               "OPENSHIFT_BUILD_NAMESPACE=testing",
               "OPENSHIFT_BUILD_SOURCE=https://github.com/jcpowermac/mysql-container",
               "OPENSHIFT_BUILD_COMMIT=a4043f50f66cd3fd30feb178bc7b680f358ff61a"
            ],
            "Entrypoint":[
               "container-entrypoint"
            ]
         },
         "Config":{
            "Hostname":"d69d8d473e5c",
            "Volumes":{
               "/var/lib/mysql/data":{

               }
            },
            "Image":"sha256:2d2ac08e0333cc3150f7eef388e6b172ed7d31a7ad8d47509b0af73697b7ef3e",
            "Cmd":[
               "run-mysqld"
            ],
            "Labels":{
               "io.k8s.description":"MySQL is a multi-user, multi-threaded SQL database server",
               "io.openshift.build.commit.author":"Joseph Callen \\\\u003cjcpowermac@gmail.com\\\\u003e",
               "io.openshift.build.commit.message":"Changes to support utf8",
               "Version":"5.6",
               "vcs-ref":"08780b7a7779335cf28f64654e43c75ad9341c77",
               "Vendor":"Red Hat, Inc.",
               "io.k8s.display-name":"MySQL 5.6",
               "io.openshift.build.source-context-dir":"5.6",
               "io.openshift.build.commit.date":"Tue Nov 8 16:50:52 2016 -0500",
               "Authoritative_Registry":"registry.access.redhat.com",
               "distribution-scope":"public",
               "Name":"rhscl/mysql-56-rhel7",
               "Build_Host":"rcm-img-docker02.build.eng.bos.redhat.com",
               "io.openshift.build.commit.ref":"master",
               "vcs-type":"git",
               "Architecture":"x86_64",
               "Release":"1",
               "BZComponent":"rh-mysql56-docker",
               "build-date":"2016-09-06T14:12:54.553894Z",
               "io.openshift.build.source-location":"https://github.com/jcpowermac/mysql-container",
               "summary":"MySQL is a multi-user, multi-threaded SQL database server",
               "architecture":"x86_64",
               "io.openshift.build.commit.id":"a4043f50f66cd3fd30feb178bc7b680f358ff61a",
               "release":"104",
               "io.openshift.expose-services":"3306:mysql",
               "io.openshift.tags":"database,mysql,mysql56,rh-mysql56",
               "com.redhat.build-host":"rcm-img-docker02.build.eng.bos.redhat.com"
            },
            "ExposedPorts":{
               "3306/tcp":{

               }
            },
            "User":"27",
            "Env":[
               "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
               "container=docker",
               "MYSQL_VERSION=5.6",
               "HOME=/var/lib/mysql",
               "CONTAINER_SCRIPTS_PATH=/usr/share/container-scripts/mysql",
               "MYSQL_PREFIX=/opt/rh/rh-mysql56/root/usr",
               "ENABLED_COLLECTIONS=rh-mysql56",
               "BASH_ENV=/usr/share/container-scripts/mysql/scl_enable",
               "ENV=/usr/share/container-scripts/mysql/scl_enable",
               "PROMPT_COMMAND=. /usr/share/container-scripts/mysql/scl_enable",
               "OPENSHIFT_BUILD_NAME=mysql-container-1",
               "OPENSHIFT_BUILD_NAMESPACE=testing",
               "OPENSHIFT_BUILD_SOURCE=https://github.com/jcpowermac/mysql-container",
               "OPENSHIFT_BUILD_COMMIT=a4043f50f66cd3fd30feb178bc7b680f358ff61a"
            ],
            "Entrypoint":[
               "container-entrypoint"
            ]
         },
         "Id":"c2738aa9362b2028d55603700736b98f824e3a96123bd88243190036281b1e21",
         "Size":133933118
      }
   },
   "apiVersion":"v1",
   "metadata":{
      "creationTimestamp":null,
      "namespace":"testing",
      "name":"mysql-container@664c4f8",
      "selfLink":"/oapi/v1/namespaces/testing/imagestreamimages/mysql-container@664c4f8"
   }
}
```
