State of the OSL 2019
=====================
:slug: state-of-osl-2019
:date: 2019-04-07
:author: Lance Albertson
:tag: featured-stories

It's been a while since we've written about what we have been up to lately. We tend to spend more time working on the
engineering side of the lab and less on writing blogs. I wanted to change that and give an update on what we've been up
to in the past year.

In March, I attended SCALE 17x in Pasadena, California and gave a talk about the state of the lab. It was also recently
featured on LWN.net which also gives a great overview. I'm going to discuss a few of those topics here, but if you want
to read more specifics, please check out the article and also watch the video of the talk.

Major projects in the past year
-------------------------------

Over the past year, we've been quite busy updating our infrastructure to meet the needs of FOSS projects. Some of the
more notable projects include:

- Deployment of a Ceph storage cluster
- Deployment of an x86-based OpenStack cluster
- 10g network deployment
- CI / CD bare metal infrastructure deployment
- Migration of legacy systems to Chef and CentOS 7
- Storage upgrade on FTP mirroring servers
- Deployment of POWER9 on our OpenPOWER Openstack Cluster
- Deployment of Grafana and Prometheus metrics monitoring

Many of these projects were completed thanks to many hardware donations from various companies which include:

- Hudson River Trading (10g Arista switches)
- Facebook (3 racks and 90 nodes of OCP compute nodes)
- Intel (20 x 10G NICs, 8 NVMe 800G drives)
- IBM (POWER9 and HDDs for FTP storage upgrade)
- Dell/EMC (8 x compute nodes for x86 OpenStack cluster, 2 x 10g Arista switches)

Progression into the cloud
--------------------------

While we have offered cloud-like services via our Ganeti clusters for the past ten years, we have lagged behind on
catching up to meet the demands of modern cloud computing services. We have invested a lot of time and energy to build
and deploy new cloud friendly services in the past several years. OpenStack seems to meet most of those demands since
it provides a stable API, a wide variety of cloud services and an active community.

We've been using OpenStack since around 2013 internally, however given the maturity of the project at the time, we
weren't quite ready to open it up for general project use. We deployed our first production OpenStack cluster in 2015
which powers a development platform for the POWER ecosystem. This allowed us to learn how to not only deploy but also
maintain and tweak an OpenStack cluster. Along the way, we converted the cluster from using local LVM-based storage, to
software defined using using Ceph which greatly improved performance and reliability.

In 2018 finally deployed an x86-based cluster which was also powered with a new Ceph cluster. At this point, we felt
the infrastructure was mature and stable enough to finally offer it to projects. Since then, we have around a dozen or
more projects using the cluster, with plenty of capacity to add more. Projects can request access to this cluster using
our hosting form for free.

CI / CD resources
-----------------

Most projects these day use some kind of continuous integration and/or continuous delivery service whether that is
using something like Travis-CI, CircleCI or using something like Jenkins on a public cloud such as AWS. We started
seeing more projects running into limitations using those free services or issues paying for the public cloud
instances.

Thanks to a donation from Facebook in 2016, we acquired three OCP racks with a total of 90 compute nodes and 80 x 3TB
SATA drives. This donation was also made possible through a collaboration with the GCC Compile Farm Project.  Because
of some limitations we ran into getting this hardware up and running, we didn't get this setup and ready until 2018. We
currently now have around 60+ nodes allocated to various projects for their CI/CD needs.

Financial status
----------------

TODO

Goals for 2019
--------------

- Finish our migrations from legacy systems to Chef and CentOS 7
- Start replacing our aging network infrastructure core
- Deploy an ARM-based OpenStack cluster
- Replacing aging compute and storage hardware
- OCP rack(s) that are compatible with our data center donated
- Expanding our Ceph cluster storage
- Migrating and upgrading our Chef infrastructure to support Chef 14
- Deploy an HA PostgreSQL cluster
- Prepare our infrastructure of CentOS 8
