FROM python:3.5.3

ENV cmake_version 3.7.1
ENV madeline_git_commit master
ENV madeline_git_url https://github.com/piratical/Madeline_2.0_PDE

RUN pwd

RUN mkdir /app

RUN apt-get update \
      && apt-get install -y --force-yes --no-install-recommends \
           gettext \
           vim \
      && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /build

RUN curl -sSL https://cmake.org/files/v${cmake_version%.*}/cmake-${cmake_version}.tar.gz | tar zxf - \
      && cd cmake-${cmake_version} \
      && ./configure \
      && make -j$(nproc) install \
      && cd - \
      && rm -rf cmake-${cmake_version}

RUN git clone ${madeline_git_url} madeline \
      && cd madeline \
      && git checkout ${madeline_commit} \
      && git show --format="${madeline_git_url}/tree/%h - %ci" ${madeline_git_commit} > /app/madeline-version.txt \
      && cat /app/madeline-version.txt \
      && ./configure \
      && make -j$(nproc) install \
      && cd - \
      && rm -rf madeline

WORKDIR /app

COPY madeline/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY madeline/. .

CMD ["gunicorn", "--bind=0.0.0.0:5000", "--workers=8", "server:app"]
