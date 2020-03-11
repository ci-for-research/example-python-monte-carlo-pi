#include "scientific_module.hpp"
#include <algorithm>
#include <iostream>
#include <math.h>
#include <random>
#include <thread>
namespace py = pybind11;

double compute_pi_cpp(int samples) {
  // Take random x and y cartesian coordinates

  auto xs = create_random_vector(samples);
  auto ys = create_random_vector(samples);

  auto inside = 0.0;
  for (auto i = 0; i < samples; i++) {
    auto x = sqrt(pow(xs[i], 2.0) + pow(ys[i], 2.0));
    if (x < 1.0) {
      inside += 1.0;
    }
  }
  // return approx_pi
  return 4 * inside / static_cast<double>(samples);
}

std::vector<double> create_random_vector(int samples) {
  // Will be used to obtain a seed for the random number engine
  std::random_device rd;
  // Standard mersenne_twister_engine seeded with rd()
  std::mt19937 gen(rd());
  std::uniform_real_distribution<> dist(0.0, 1.0);
  std::vector<double> xs(samples);
  std::generate(xs.begin(), xs.end(), [&]() { return dist(gen); });
  return xs;
}

// Python interface definition
PYBIND11_MODULE(compute_pi_cpp, m) {
  m.doc() = "Compute the pi number using the Monte Carlo method";

  m.def("compute_pi_cpp", &compute_pi_cpp,
        R"pdoc(Compute pi using the Monte Carlo method
     
            Args:
               samples (int): Number of samples
       )pdoc",
        py::arg("samples"));
}
