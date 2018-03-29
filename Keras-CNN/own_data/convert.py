import coremltools


output_labels = ['cats','dogs','horses','humans']


coreml_model = coremltools.converters.keras.convert('model.h5',
													input_names='image',
													image_input_names='image',
													output_names='output',
													class_labels= ['cats','dogs','horses','humans']
													)


coreml_model.author = 'Jakub Tlach'
coreml_model.license = 'MIT'
coreml_model.short_description = 'Model to classify hand written digit'
coreml_model.input_description['image'] = 'Grayscale image of hand written digit'
coreml_model.output_description['output'] = 'Predicted digit'

coreml_model.save('modelcnn.mlmodel')