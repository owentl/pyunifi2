pkgname=python-pyunifi
pkgver=r256.cf2c735
pkgrel=1
pkgdesc='A rewrite of https://github.com/unifi-hackers/unifi-lab in cleaner Python.'
arch=('any')
url='https://github.com/BoostCookie/pyunifi'
license=('MIT')
depends=('python-requests')
makedepends=('python-setuptools')
source=("${pkgname}::git+https://github.com/BoostCookie/pyunifi.git")
md5sums=('SKIP')

pkgver() {
	cd "$pkgname"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    cd "$pkgname"
    python setup.py build
}

package() {
    cd "$pkgname"
    python setup.py install --root="$pkgdir" --optimize=1
}

