# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
from torch.testing._internal.common_methods_invocations import op_db

# Generated from codegen/gen_functorch_op_db.py via
# python codegen/gen_functorch_lagging_op_db.py > test/functorch_lagging_op_db.py
#
# People add new OpInfos to PyTorch all the time.
# We want them to be able to add OpInfos without breaking our CI.
# To achieve this, we keep our OpInfo library behind that of Pytorch's and
# we periodically update our OpInfo library by regenerating this file
_functorch_lagging_meta = {
    ('__getitem__', ''),
    ('__radd__', ''),
    ('__rand__', ''),
    ('__rdiv__', ''),
    ('__rmatmul__', ''),
    ('__rmod__', ''),
    ('__rmul__', ''),
    ('__ror__', ''),
    ('__rpow__', ''),
    ('__rsub__', ''),
    ('__rxor__', ''),
    ('abs', ''),
    ('acos', ''),
    ('acosh', ''),
    ('add', ''),
    ('addbmm', ''),
    ('addcdiv', ''),
    ('addcmul', ''),
    ('addmm', ''),
    ('addmm', 'decomposed'),
    ('addmv', ''),
    ('addr', ''),
    ('amax', ''),
    ('amin', ''),
    ('angle', ''),
    ('argmax', ''),
    ('argmin', ''),
    ('asin', ''),
    ('asinh', ''),
    ('atan', ''),
    ('atan2', ''),
    ('atanh', ''),
    ('baddbmm', ''),
    ('bitwise_left_shift', ''),
    ('bitwise_not', ''),
    ('bitwise_right_shift', ''),
    ('bmm', ''),
    ('broadcast_to', ''),
    ('cdist', ''),
    ('ceil', ''),
    ('cholesky', ''),
    ('cholesky_inverse', ''),
    ('chunk', ''),
    ('clamp', ''),
    ('clamp', 'scalar'),
    ('clone', ''),
    ('complex', ''),
    ('conj', ''),
    ('conj_physical', ''),
    ('contiguous', ''),
    ('copysign', ''),
    ('corrcoef', ''),
    ('cos', ''),
    ('cosh', ''),
    ('cov', ''),
    ('cross', ''),
    ('cummax', ''),
    ('cummin', ''),
    ('cumprod', ''),
    ('cumsum', ''),
    ('deg2rad', ''),
    ('diag', ''),
    ('diag_embed', ''),
    ('diagonal', ''),
    ('diff', ''),
    ('digamma', ''),
    ('dist', ''),
    ('div', 'floor_rounding'),
    ('div', 'no_rounding_mode'),
    ('div', 'trunc_rounding'),
    ('dot', ''),
    ('dsplit', ''),
    ('dstack', ''),
    ('eig', ''),
    ('einsum', ''),
    ('eq', ''),
    ('erf', ''),
    ('erfc', ''),
    ('erfinv', ''),
    ('exp', ''),
    ('exp2', ''),
    ('expand', ''),
    ('expand_as', ''),
    ('expm1', ''),
    ('fft.fft', ''),
    ('fft.fftn', ''),
    ('fft.hfft', ''),
    ('fft.ifft', ''),
    ('fft.ifftn', ''),
    ('fft.ihfft', ''),
    ('fft.irfft', ''),
    ('fft.irfftn', ''),
    ('fft.rfft', ''),
    ('fft.rfftn', ''),
    ('fill_', ''),
    ('flip', ''),
    ('fliplr', ''),
    ('flipud', ''),
    ('float_power', ''),
    ('floor', ''),
    ('floor_divide', ''),
    ('fmax', ''),
    ('fmin', ''),
    ('fmod', ''),
    ('fmod', 'autodiffed'),
    ('frac', ''),
    ('frexp', ''),
    ('gather', ''),
    ('ge', ''),
    ('geqrf', ''),
    ('gradient', ''),
    ('gt', ''),
    ('histogram', ''),
    ('hsplit', ''),
    ('hstack', ''),
    ('hypot', ''),
    ('i0', ''),
    ('imag', ''),
    ('index_add', ''),
    ('index_copy', ''),
    ('index_fill', ''),
    ('index_put', ''),
    ('index_select', ''),
    ('inner', ''),
    ('inverse', ''),
    ('isin', ''),
    ('kron', ''),
    ('kthvalue', ''),
    ('le', ''),
    ('lerp', ''),
    ('lgamma', ''),
    ('linalg.cholesky', ''),
    ('linalg.cholesky_ex', ''),
    ('linalg.cond', ''),
    ('linalg.det', ''),
    ('linalg.eig', ''),
    ('linalg.eigh', ''),
    ('linalg.eigvals', ''),
    ('linalg.eigvalsh', ''),
    ('linalg.householder_product', ''),
    ('linalg.inv', ''),
    ('linalg.inv_ex', ''),
    ('linalg.lstsq', ''),
    ('linalg.matrix_norm', ''),
    ('linalg.matrix_power', ''),
    ('linalg.matrix_rank', ''),
    ('linalg.matrix_rank', 'hermitian'),
    ('linalg.multi_dot', ''),
    ('linalg.norm', ''),
    ('linalg.pinv', ''),
    ('linalg.pinv', 'hermitian'),
    ('linalg.qr', ''),
    ('linalg.slogdet', ''),
    ('linalg.solve', ''),
    ('linalg.svd', ''),
    ('linalg.svdvals', ''),
    ('linalg.vector_norm', ''),
    ('log', ''),
    ('log10', ''),
    ('log1p', ''),
    ('log2', ''),
    ('log_softmax', ''),
    ('log_softmax', 'dtype'),
    ('logaddexp', ''),
    ('logaddexp2', ''),
    ('logcumsumexp', ''),
    ('logdet', ''),
    ('logical_not', ''),
    ('logit', ''),
    ('logsumexp', ''),
    ('lt', ''),
    ('lu', ''),
    ('lu_unpack', ''),
    ('masked_fill', ''),
    ('masked_scatter', ''),
    ('masked_select', ''),
    ('matmul', ''),
    ('matrix_exp', ''),
    ('max', 'binary'),
    ('max', 'reduction_no_dim'),
    ('max', 'reduction_with_dim'),
    ('maximum', ''),
    ('mean', ''),
    ('median', ''),
    ('min', 'binary'),
    ('min', 'reduction_no_dim'),
    ('min', 'reduction_with_dim'),
    ('minimum', ''),
    ('mm', ''),
    ('mode', ''),
    ('movedim', ''),
    ('msort', ''),
    ('mul', ''),
    ('mv', ''),
    ('mvlgamma', 'mvlgamma_p_1'),
    ('mvlgamma', 'mvlgamma_p_3'),
    ('mvlgamma', 'mvlgamma_p_5'),
    ('nan_to_num', ''),
    ('nanmedian', ''),
    ('nanquantile', ''),
    ('nansum', ''),
    ('narrow', ''),
    ('ne', ''),
    ('neg', ''),
    ('nn.functional.gelu', ''),
    ('nn.functional.hardshrink', ''),
    ('nn.functional.hardswish', ''),
    ('nn.functional.hardtanh', ''),
    ('nn.functional.leaky_relu', ''),
    ('nn.functional.logsigmoid', ''),
    ('nn.functional.relu6', ''),
    ('norm', ''),
    ('norm', 'fro'),
    ('norm', 'inf'),
    ('norm', 'nuc'),
    ('ormqr', ''),
    ('outer', ''),
    ('permute', ''),
    ('pinverse', ''),
    ('polar', ''),
    ('polygamma', 'polygamma_n_0'),
    ('polygamma', 'polygamma_n_1'),
    ('polygamma', 'polygamma_n_2'),
    ('polygamma', 'polygamma_n_3'),
    ('polygamma', 'polygamma_n_4'),
    ('positive', ''),
    ('pow', ''),
    ('prod', ''),
    ('put', ''),
    ('qr', ''),
    ('quantile', ''),
    ('rad2deg', ''),
    ('ravel', ''),
    ('real', ''),
    ('reciprocal', ''),
    ('remainder', ''),
    ('remainder', 'autodiffed'),
    ('renorm', ''),
    ('repeat', ''),
    ('reshape', ''),
    ('reshape_as', ''),
    ('resize_', ''),
    ('resize_as_', ''),
    ('resolve_conj', ''),
    ('resolve_neg', ''),
    ('roll', ''),
    ('rot90', ''),
    ('round', ''),
    ('rsqrt', ''),
    ('rsub', 'rsub_scalar'),
    ('rsub', 'rsub_tensor'),
    ('scatter', ''),
    ('scatter_add', ''),
    ('select', ''),
    ('sgn', ''),
    ('sigmoid', ''),
    ('sign', ''),
    ('signbit', ''),
    ('sin', ''),
    ('sinc', ''),
    ('sinh', ''),
    ('solve', ''),
    ('sort', ''),
    ('special.entr', ''),
    ('special.erfcx', ''),
    ('special.i0e', ''),
    ('special.i1', ''),
    ('special.i1e', ''),
    ('special.ndtr', ''),
    ('special.ndtri', ''),
    ('special.polygamma', 'special_polygamma_n_0'),
    ('special.xlog1py', ''),
    ('special.zeta', ''),
    ('special.zeta', 'grad'),
    ('split', ''),
    ('split', 'list_args'),
    ('split_with_sizes', ''),
    ('sqrt', ''),
    ('square', ''),
    ('squeeze', ''),
    ('stack', ''),
    ('std', ''),
    ('std_mean', ''),
    ('sub', ''),
    ('sum', ''),
    ('svd', ''),
    ('symeig', ''),
    ('t', ''),
    ('take', ''),
    ('take_along_dim', ''),
    ('tan', ''),
    ('tanh', ''),
    ('tensor_split', ''),
    ('tensordot', ''),
    ('tile', ''),
    ('to_sparse', ''),
    ('topk', ''),
    ('trace', ''),
    ('transpose', ''),
    ('triangular_solve', ''),
    ('tril', ''),
    ('triu', ''),
    ('true_divide', ''),
    ('trunc', ''),
    ('unfold', ''),
    ('unsqueeze', ''),
    ('var', ''),
    ('var_mean', ''),
    ('vdot', ''),
    ('view', ''),
    ('view_as', ''),
    ('view_as_complex', ''),
    ('view_as_real', ''),
    ('vsplit', ''),
    ('vstack', ''),
    ('where', ''),
    ('xlogy', ''),
    ('zero_', ''),
}


def in_functorch_lagging_op_db(opinfo):
    return (opinfo.name, opinfo.variant_test_name) in _functorch_lagging_meta


functorch_lagging_op_db = [
    opinfo for opinfo in op_db if in_functorch_lagging_op_db(opinfo)
]